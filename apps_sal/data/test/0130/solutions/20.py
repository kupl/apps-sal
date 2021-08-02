n, m = [int(s) for s in input().split()]
g = [[0 for i in range(m)] for j in range(n)]
sum = 0
top = n - 1
bottom = 0
left = m - 1
right = 0
for i in range(n):
    f = str(input())
    for j in range(m):
        if f[j] == 'B':
            sum += 1
            top = min(top, i)
            bottom = max(bottom, i)
            left = min(left, j)
            right = max(right, j)
if sum == 0:
    print(1)
else:
    a = max(right - left + 1, bottom - top + 1)
    if a > n or a > m:
        print(-1)
    else:
        print(a**2 - sum)
