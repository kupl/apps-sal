(N, M) = map(int, input().split())
(L, R) = ([0] * M, [0] * M)
A = set(range(N))
(lm, rm) = (0, N)
for i in range(M):
    (L[i], R[i]) = map(int, input().split())
    lm = max(lm, L[i])
    rm = min(rm, R[i])
if lm <= rm:
    print(rm - lm + 1)
else:
    print(0)
