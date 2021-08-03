mem = [[-1, -1] for x in range(0, 103)]

n, k, d = list(map(int, input().split()))


def dp(remain, has_d):
    if remain == 0:
        return has_d
    if remain < 0:
        return 0
    if mem[remain][has_d] != -1:
        return mem[remain][has_d]
    mem[remain][has_d] = 0
    for i in range(1, min(remain, k) + 1):
        if i >= d:
            mem[remain][has_d] += dp(remain - i, 1)
        else:
            mem[remain][has_d] += dp(remain - i, has_d)
    return mem[remain][has_d]


print(dp(n, 0) % (10**9 + 7))
