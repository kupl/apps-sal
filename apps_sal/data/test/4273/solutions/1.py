from collections import Counter
n = int(input())
s = [input() for _ in range(n)]
cnt = 0
c = Counter((x[0] for x in s))
for x in s:
    if x[0] in 'MARCH':
        cnt += 1
ans = cnt * (cnt - 1) * (cnt - 2) // 6
for (k, v) in list(c.items()):
    if k not in 'MARCH':
        continue
    if v >= 2:
        ans -= v * (v - 1) // 2 * (cnt - v)
    if v >= 3:
        ans -= v * (v - 1) * (v - 2) // 6
print(ans)
