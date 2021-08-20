n = int(input())
m = n - 1
cn = {}
for i in range(1, n + 1):
    cn[i] = set()
for _ in range(m):
    (a, b) = list(map(int, input().split()))
    cn[a].add(b)
    cn[b].add(a)
ans = 0
for i in range(1, n + 1):
    ans += sum((len(cn[c]) for c in cn[i])) - len(cn[i])
print(ans // 2)
