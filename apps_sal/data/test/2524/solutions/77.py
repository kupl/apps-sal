(N, *A) = list(map(int, open(0).read().split()))
print(sum(((b := (1 << i)) * (z := sum((1 for a in A if a & b == 0))) * (N - z) % (mod := (10 ** 9 + 7)) for i in range(60))) % mod)
