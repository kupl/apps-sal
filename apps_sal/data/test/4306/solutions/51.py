A, B, C, D = list(map(int, input().split()))

alice = [1 if A <= t < B else 0 for t in range(0, 110)]
bob = [1 if C <= t < D else 0 for t in range(0, 110)]

overlap = [1 for a, b in zip(alice, bob) if a > 0 and b > 0]

print((len(overlap)))
