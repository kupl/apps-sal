n = int(input())
ar = list(map(int, input().split()))
k25 = 0
k50 = 0
for i in range(n):
    if ar[i] == 25:
        k25 += 1
    elif ar[i] == 50:
        k25 -= 1
        k50 += 1
    elif k50 >= 1:
        k25 -= 1
        k50 -= 1
    else:
        k25 -= 3
    if k25 < 0:
        break
if k25 < 0:
    print('NO')
else:
    print('YES')
