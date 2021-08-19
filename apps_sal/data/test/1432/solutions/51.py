N = int(input())
A = tuple(map(int, input().split()))
r = [0] * N
for (i, a) in enumerate(A):
    if i % 2 == 0:
        r[0] += a
    else:
        r[0] -= a
r[-1] = 2 * A[-1] - r[0]
for i in range(N - 2, 0, -1):
    r[i] = 2 * A[i] - r[i + 1]
ans = ' '.join(map(str, r))
print(ans)
