import itertools
(N, M, Q) = map(int, input().split())
a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q
for i in range(Q):
    (a[i], b[i], c[i], d[i]) = map(int, input().split())
cc = [i for i in range(1, M + 1)]
ans = 0
for A in itertools.combinations_with_replacement(cc, N):
    A = list(A)
    t = 0
    for i in range(Q):
        if A[b[i] - 1] - A[a[i] - 1] == c[i]:
            t += d[i]
    ans = max(ans, t)
print(ans)
