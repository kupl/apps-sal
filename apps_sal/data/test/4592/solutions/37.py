MOD = 10**9 + 7
memo = [0] * 10000

N = int(input())


def primeLst(k):
    acc = []
    if k == 1:
        return acc
    f = 2
    while f * f <= k:
        if k % f == 0:
            acc.append(f)
            k //= f
        else:
            f += 1
    if k != 1:
        acc.append(k)
    return acc


for i in range(N):
    l = primeLst(i + 1)
    for x in l:
        memo[x] += 1

res = 1
for i in range(1, N):
    res *= memo[i + 1] + 1
    res %= MOD

print(res)
