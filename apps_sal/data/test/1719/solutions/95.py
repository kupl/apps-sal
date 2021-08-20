import re


def ok(last4):
    pattern = '.?AGC.?|.?GAC.?|.?ACG.?|A.GC|AG.C'
    res = re.match(pattern, last4)
    return res is None


def dfs(cur, last3, n, m, mod):
    if last3 in m[cur]:
        return m[cur][last3]
    if cur == n:
        return 1
    ret = 0
    for c in 'ACGT':
        if ok(last3 + c):
            ret = (ret + dfs(cur + 1, last3[1:] + c, n, m, mod)) % mod
    m[cur][last3] = ret
    return ret


def main():
    n = int(input())
    mod = 10 ** 9 + 7
    m = [{} for _ in range(n + 1)]
    ans = dfs(0, 'TTT', n, m, mod)
    print(ans)


def __starting_point():
    main()


__starting_point()
