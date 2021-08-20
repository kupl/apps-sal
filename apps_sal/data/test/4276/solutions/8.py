(n, t) = map(int, input().split())
data = [input().split() for i in range(n)]
ans = 1001
for i in range(n):
    if int(data[i][1]) <= t:
        ans = min(ans, int(data[i][0]))
if ans == 1001:
    print('TLE')
else:
    print(ans)
