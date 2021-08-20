import itertools
(N, M, Q) = list(map(int, input().split()))
a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q
for i in range(Q):
    (a[i], b[i], c[i], d[i]) = list(map(int, input().split()))
l = list(range(1, M + 1))
i = 0
D = []
for v in itertools.combinations_with_replacement(l, N):
    D.append(0)
    for j in range(Q):
        if v[b[j] - 1] - v[a[j] - 1] == c[j]:
            D[i] += d[j]
    i += 1
print(max(D))
