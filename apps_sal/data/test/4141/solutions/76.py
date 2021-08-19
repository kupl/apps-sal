n = int(input())
a = [int(i) for i in input().split()]
q = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        if a[i] % 3 == 0 or a[i] % 5 == 0:
            q += 1
    else:
        q += 1
if q == len(a):
    print('APPROVED')
else:
    print('DENIED')
