(n, T) = map(int, input().split())
ans = 10000
for i in range(n):
    (c, t) = map(int, input().split())
    if t <= T:
        ans = min(ans, c)
if ans == 10000:
    print('TLE')
else:
    print(ans)
