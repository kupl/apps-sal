(a, b, c, d) = map(int, input().split())
alice = set((i for i in range(a, b + 1)))
bob = set((j for j in range(c, d + 1)))
s = alice & bob
print(max(len(alice & bob) - 1, 0))
