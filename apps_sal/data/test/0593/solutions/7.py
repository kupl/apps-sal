(n, m) = list(map(int, input().split()))
k = [0] * n
for i in range(m):
    l = list(map(int, input().split()))
    t = max(l)
    k[l.index(t)] += 1
t = max(k)
print(k.index(t) + 1)
