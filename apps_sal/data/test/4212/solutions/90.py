import itertools

N, M, Q = map(int, input().split())
a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q
for i in range(Q):
    a[i], b[i], c[i], d[i] = map(int, input().split())
    a[i] -= 1
    b[i] -= 1

result = 0
for A in itertools.combinations_with_replacement(range(1, M + 1), N):
    score = 0
    for i in range(Q):
        if A[b[i]] - A[a[i]] == c[i]:
            score += d[i]
    result = max(result, score)
print(result)
