from itertools import count
with open(0) as f:
    N, *p = map(int, f.read().split())
p.append(N + 1)
ans = 0
for i in count(0):
    if i == N:
        break
    if p[i] == i + 1:
        p[i] = p[i + 1]
        p[i + 1] = i + 1
        ans += 1
print(ans)
