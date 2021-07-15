n, t = map(int, input().split())
ans = 1001001001

for _ in range(n):
    ci, ti = map(int, input().split())
    if ti <= t:
        ans = min(ans, ci)

if ans == 1001001001:
    print('TLE')
else:
    print(ans)
