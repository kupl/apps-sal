import sys
sys.setrecursionlimit(10 ** 7)


def main(n, ab):
    f = [[-1, -1] for _ in range(2 * n)]
    mi = set(range(2 * n))
    for (i, (a, b)) in enumerate(ab):
        (a, b) = (a - 1, b - 1)
        if a >= 0 and a not in mi:
            return False
        if b >= 0 and b not in mi:
            return False
        if a >= 0 and b >= 0 and (a >= b):
            return False
        mi.discard(a)
        mi.discard(b)
        if a >= 0 and b >= 0:
            f[a][0] = 1
            f[a][1] = i
            f[b][0] = 0
            f[b][1] = i
        elif a >= 0:
            f[a][0] = 1
            f[a][1] = i
        elif b >= 0:
            f[b][0] = 0
            f[b][1] = i
    if f[0][0] == 0:
        return False
    if f[-1][0] == 1:
        return False
    now = 0
    memo = {}

    def chk(l, r):
        if (l, r) in memo:
            return memo[l, r]
        if (r - l) % 2 == 0:
            return False
        ret = True
        ci = (r - l) // 2
        rid = []
        for i in range(l, l + ci + 1):
            if f[i][0] == 0:
                ret = False
            rid.append(f[i][1])
        j = 0
        for i in range(l + ci + 1, r + 1):
            if f[i][0] == 1:
                ret = False
            if rid[j] != -1 and f[i][1] != -1 and (rid[j] != f[i][1]):
                ret = False
            j += 1
        memo[l, r] = ret
        return ret

    def dp(l):
        if l == 2 * n:
            return True
        ret = False
        for ri in range(l + 1, 2 * n):
            tmp = chk(l, ri)
            if tmp:
                if dp(ri + 1):
                    return True
        return False
    dp(0)
    return dp(0)


n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
ret = main(n, ab)
print('Yes' if ret else 'No')
