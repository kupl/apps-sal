N, K = list(map(int, input().split()))
S = []

for i in range(K):
    l, r = list(map(int, input().split()))
    S.append([l, r])

d = {}
acc = {}


def get_acc_num(i, l, r):
    if i - l <= 0:
        return 0
    if i - r <= 0:
        return acc[i - l]
    else:
        return acc[i - l] - acc[i - r - 1]


MOD = 998244353
for i in range(1, N + 1):
    # print(f"{i}-------------------")
    if i == 1:
        d[i] = 1
        acc[0] = 0
        acc[i] = 1
    else:
        d[i] = 0
        for l, r in S:
            # print(f"{l, r}")
            # print(get_acc_num(i, l, r))
            # print(get_acc_num(i, l, r))
            d[i] += get_acc_num(i, l, r) % MOD
            acc[i] = (acc[i - 1] + d[i]) % MOD

print((d[N] % 998244353))
