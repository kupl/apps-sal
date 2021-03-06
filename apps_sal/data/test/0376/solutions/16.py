from collections import Counter
n = int(input())
a = list((int(v) for v in input().split())) + [-1000000002]
c = Counter(a)
(top, sec) = sorted(set(a))[-1:-3:-1]
topC = [1 if v == top else 0 for v in a]
secC = [1 if v == sec else 0 for v in a]
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
    if topC[i] < c[top]:
        continue
    best = top if topC[i] == 1 and a[i] == top else top + 1
    if secC[i] < c[sec]:
        best = max(best, sec + 2)
    ans = min(ans, best)
print(ans)
