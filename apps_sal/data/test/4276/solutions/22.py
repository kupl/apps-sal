(n, t) = map(int, input().split())
ans = 10000
for i in range(n):
    (a, b) = map(int, input().split())
    if b <= t:
        ans = min(ans, a)
if ans < 10000:
    print(ans)
else:
    print('TLE')
