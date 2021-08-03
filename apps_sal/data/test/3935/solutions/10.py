n = int(input())
dists = list(map(int, input().split()))
pow2 = [[] for _ in range(64)]
Set = [0] * n
for i in range(n):
    ds = d = dists[i]
    powd = 0
    while d % 2 == 0:
        d >>= 1
        powd += 1
    pow2[powd].append(ds)
    Set[i] = powd
maxset = max(range(64), key=lambda x: len(pow2[x]))
print(n - len(pow2[maxset]))
for i in range(n):
    if Set[i] != maxset:
        print(dists[i], end=" ")
