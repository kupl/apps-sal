from collections import defaultdict, Counter
n = int(input())
a = list((int(v) for v in input().split())) + [-1000000002]
c = Counter(a)
(top, sec) = sorted(set(a))[-1:-3:-1]
(topC, secC) = ([0] * n, [0] * n)
for i in range(n - 1):
    (u, v) = (int(v) for v in input().split())
    if a[u - 1] == top:
        topC[v - 1] += 1
    if a[v - 1] == top:
        topC[u - 1] += 1
    if a[u - 1] == sec:
        secC[v - 1] += 1
    if a[v - 1] == sec:
        secC[u - 1] += 1
ans = top + 2
for i in range(n):
    add = 1 if a[i] == top else 0
    if topC[i] + add < c[top]:
        continue
    best = top + 1 if topC[i] else top
    add = 1 if a[i] == sec else 0
    if secC[i] + add < c[sec]:
        best = max(best, sec + 2)
    ans = min(ans, best)
print(ans)
