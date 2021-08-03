n, t = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
l = list(sorted(l, key=lambda x: x[1]))
c, m = [list(i) for i in zip(*l)]
ans = 9999
for i in range(n):
    if m[i] > t:
        break
    else:
        ans = min(ans, c[i])
if ans == 9999:
    print('TLE')
else:
    print(ans)
