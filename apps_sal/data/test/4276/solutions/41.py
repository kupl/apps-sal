(a, b) = map(int, input().split())
ans = []
for i in range(a):
    (c, d) = map(int, input().split())
    if d <= b:
        ans.append(c)
print('TLE' if len(ans) == 0 else min(ans))
