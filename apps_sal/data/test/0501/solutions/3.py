(l, r) = [int(e) for e in input().split()]
MOD = 1000000007


def sum_range(start, num):
    end = start + (num - 1) * 2
    return (start + end) * num // 2


def sum(n):
    ans = 0
    s = [1, 2]
    cnt = 1
    which = 0
    while n > 0:
        diff = min(n, cnt)
        ans += sum_range(s[which], diff)
        ans %= MOD
        s[which] += 2 * diff
        n -= diff
        cnt *= 2
        which = 1 - which
    return ans


print(((sum(r) - sum(l - 1)) % MOD + MOD) % MOD)
