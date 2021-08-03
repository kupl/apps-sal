n, r, avg = list(map(int, input().split()))
score = []
total = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    score.append((b, a))
    total += a
need_point = max(0, avg * n - total)
score.sort()
ans = 0
for b, a in score:
    if need_point == 0:
        break
    if a < r:
        ans += b * min(r - a, need_point)
        need_point -= min(r - a, need_point)
print(ans)
