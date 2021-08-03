n, T = list(map(int, input().split()))
ans = 10**3 + 1
for i in range(n):
    c, t = list(map(int, input().split()))
    if t > T:
        continue
    else:
        ans = min(ans, c)
if ans == 10**3 + 1:
    print('TLE')
else:
    print(ans)
