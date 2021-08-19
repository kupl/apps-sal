n = int(input())
a = input()
a = a.split()
c = 0
for b in range(n):
    if int(a[b]) % 3 == 0 or int(a[b]) % 5 == 0 or int(a[b]) % 2 == 1:
        c = c + 1
if c == n:
    print('APPROVED')
else:
    print('DENIED')
