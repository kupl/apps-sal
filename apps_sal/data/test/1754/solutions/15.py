n, m, k = map(int, input().split())
best = [(0, 0) for i in range(m)]
w = list(map(int, input().split()))
s = list(map(int, input().split()))
st = set(list(map(int, input().split())))
for i in range(n):
    best[s[i] - 1] = max((w[i], i + 1), best[s[i] - 1])
for e in best:
    k -= (e[1] in st)
print(k)
