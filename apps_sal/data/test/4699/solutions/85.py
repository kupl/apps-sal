N, K, *D = list(map(int, open(0).read().split()))
D = set(str(d) for d in D)
for i in range(N, 100_000):
    if set(str(i)) & D:
        continue
    print(i)
    break
