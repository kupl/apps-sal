from collections import defaultdict
INF = float('inf')
(N, *A) = map(int, open(0).read().split())
I = defaultdict(lambda: -INF)
O = defaultdict(lambda: -INF)
O[0, 0] = 0
for (i, a) in enumerate(A, 1):
    j = (i - 1) // 2
    for n in [j, j + 1]:
        I[i, n] = a + O[i - 1, n - 1]
        O[i, n] = max(O[i - 1, n], I[i - 1, n])
print(max(I[N, N // 2], O[N, N // 2]))
