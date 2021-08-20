(N, K) = list(map(int, input().split()))


def absolute(x):
    x = x - K
    if x < 0:
        x = -x
    return x


if N < K:
    while N > abs(N - K):
        N = absolute(N)
    print(N)
elif N % K == 0:
    print(0)
else:
    b = 1
    s = K
    while b > 0 and N > abs(N - s):
        b = N % K
        N = K
        a = K
        K = b
    print(a)
