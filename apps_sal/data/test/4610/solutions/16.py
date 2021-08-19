(n, k) = map(int, input().split())
A = list(map(int, input().split()))
d = {}
for a in A:
    d[a] = d.get(a, 0) + 1
if len(d) <= k:
    print(0)
else:
    d = sorted(d.values())
    cnt = 0
    for i in range(len(d) - k):
        cnt += d[i]
    print(cnt)
