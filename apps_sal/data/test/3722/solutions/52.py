N = int(input())
c = "".join(input() for _ in range(4))

M = 10**9+7
if c in ("AAAA", "AAAB", "AABA", "AABB", "ABAB", "ABBB", "BBAB", "BBBB"):
  print((1))
if c in ("ABAA", "BABA", "BABB", "BBAA"):
  print((pow(2, max(0, N-3), M)))
if c in ("ABBA", "BAAA", "BAAB", "BBBA"):
  F = [1, 1]
  while len(F)<=N:
    F += [(F[-1]+F[-2])%M]
  print((F[N-2]))

