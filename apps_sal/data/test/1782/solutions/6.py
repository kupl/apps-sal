(n, k) = list(map(int, input().split()))
if n // k < 3:
    print(-1)
else:
    v = [0] * n
    for i in range(k):
        v[2 * i] = v[2 * i + 1] = i + 1
    for i in range(2 * k, n):
        v[i] = (i - 2 * k) % k + 1
    print(' '.join(map(str, v)))
