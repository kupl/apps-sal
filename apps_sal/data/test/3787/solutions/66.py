(N, A, B) = map(int, input().split())
a = list(range(N - A + 1, N + 1))
for i in range(B - 1, 0, -1):
    a.append(i)
(m, M) = (B, N - A)
for j in range(A - 1):
    for i in range(min(M, m + B - 2), m - 1, -1):
        a.append(i)
    m = min(M, m + B - 2) + 1
    if len(a) == N:
        break
print(*(a if len(a) == N else [-1]))
