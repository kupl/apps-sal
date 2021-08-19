n = int(input())
c = 0
for i in str(n):
    c += int(i)
if n % c == 0:
    print('Yes')
else:
    print('No')
