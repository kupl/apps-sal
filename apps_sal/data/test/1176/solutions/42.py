(_, *A) = map(int, open(0).read().split())
print(sum((B := [abs(a) for a in A])) - 2 * min(B) * (sum((1 for a in A if a < 0)) % 2))
