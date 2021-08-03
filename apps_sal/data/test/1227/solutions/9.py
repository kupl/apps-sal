N = input()
K = int(input())

if len(N) < K:
    print(0)
    return

ans = [1, int(N[-1]), 0, 0]


def combination(N, K):
    if N < K:
        return 0
    else:
        p = 1
        for k in range(K):
            p *= N
            N -= 1
        for k in range(1, K + 1):
            p //= k
        return p


for k in range(1, len(N)):
    if int(N[-k - 1]) > 0:
        a = [1, 0, 0, 0]
        for j in range(1, K + 1):
            a[j] += (9**(j)) * combination(k, j)
            a[j] += (int(N[-k - 1]) - 1) * combination(k, j - 1) * (9**(j - 1)) + ans[j - 1]
        ans = a
print(ans[K])
