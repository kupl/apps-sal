n, m = map(int, input().split())
p, s = [], []
for _ in range(m):
    a, b = map(str, input().split())
    p.append(a)
    s.append(b)
p = list(map(int, p))
checker = [0] * n
penalty = [0] * n
ans = 0
for i, j in enumerate(s):
    if j == "AC" and checker[p[i] - 1] == 0:
        checker[p[i] - 1] = 1
    elif j == "WA" and checker[p[i] - 1] == 0:
        penalty[p[i] - 1] += 1
for k, l in enumerate(checker):
    if l:
        ans += penalty[k]
print(sum(checker), ans)
