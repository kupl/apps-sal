(N, *A) = map(int, open(0).read().split())
print(sum(((b := (1 << i)) * (N - (z := sum((1 for a in A if a & b)))) * z % (m := (10 ** 9 + 7)) for i in range(60))) % m)
