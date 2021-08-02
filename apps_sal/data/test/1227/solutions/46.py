N = input()
K = int(input())

if len(N) < K:
    print(0)
    return

keta = []
for k in range(len(N)):
    keta.append(int(N[-k - 1]))
ans = [1, keta[0], 0, 0];


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


for k in range(1, len(N) - 1):
    if keta[k] > 0:
        a = [1, 0, 0, 0]
        for j in range(1, 4):
            a[j] += (9**(j)) * combination(k, j)
            a[j] += (keta[k] - 1) * combination(k, j - 1) * (9**(j - 1)) + ans[j - 1]
        ans = [] + a
answer = (9**(K)) * combination(len(N) - 1, K)
answer += (keta[-1] - 1) * (9**(K - 1)) * combination(len(N) - 1, K - 1)
answer += ans[K - 1]
print(answer)
