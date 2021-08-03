x, y = 0, 0
countZero = 0
countOne = 0

n, m = [int(i) for i in input().split()]
a = [0] * n


for i in range(m):
    x, y = [int(i) for i in input().split()]
    a[y - 1] += 1
    a[x - 1] += 1

for i in a:
    if i == 1:
        countZero += 1
    elif i > 1:
        countOne += 1

if n == m:
    if countZero == 0 and countOne == n:
        print('ring topology')
    else:
        print('unknown topology')
elif n - m == 1:
    if countZero == 2 and countOne == n - 2:
        print('bus topology')
    elif countZero == n - 1 and countOne == 1:
        print('star topology')
    else:
        print('unknown topology')
else:
    print('unknown topology')
