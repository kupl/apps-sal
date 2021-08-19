(N, M) = map(int, input().split())
(L, R) = (0, 10 ** 5 + 1)
for _ in range(M):
    (l, r) = map(int, input().split())
    L = max(L, l)
    R = min(R, r + 1)
if R > L:
    result = R - L
else:
    result = 0
print(result)
