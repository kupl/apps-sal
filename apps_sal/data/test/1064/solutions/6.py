n, m, k = map(int, input().split())
free = [True] * n
for i in list(map(int, input().split())):
    free[i] = False
a = list(map(int, input().split()))
last_lamp = [-1] * n
for i in range(n):
    if free[i]:
        last_lamp[i] = i
    if i > 0 and not free[i]:
        last_lamp[i] = last_lamp[i - 1]
ans = int(1E100)
for i in range(1, k + 1):
    last, prev = 0, -1
    cur = 0
    while last < n:
        if last_lamp[last] <= prev:
            cur = None
            break
        prev = last_lamp[last]
        last = prev + i
        cur += 1
    if cur is not None:
        ans = min(ans, a[i - 1] * cur)
if ans == int(1E100):
    print(-1)
else:
    print(ans)
