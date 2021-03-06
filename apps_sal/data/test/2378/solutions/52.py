import sys
sys.setrecursionlimit(10 ** 6)


def int1(x):
    return int(x) - 1


def p2D(x):
    return print(*x, sep='\n')


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def MI1():
    return map(int1, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def main():

    def dfs(u=0, pu=-1):
        res = 1
        for cu in to[u]:
            if cu == pu:
                continue
            ret = dfs(cu, u)
            children_size[u].append(ret)
            res += ret
        return res
    md = 10 ** 9 + 7
    n = II()
    to = [[] for _ in range(n)]
    for _ in range(n - 1):
        (a, b) = MI1()
        to[a].append(b)
        to[b].append(a)
    half = pow(2, md - 2, md)
    exp_half = [1, half]
    for _ in range(n):
        exp_half.append(exp_half[-1] * half % md)
    children_size = [[] for _ in range(n)]
    dfs()
    ans = 0
    noblack = exp_half[n - 1]
    for cs in children_size:
        if not cs:
            continue
        sum_cs = sum(cs)
        if sum_cs != n - 1:
            cs.append(n - 1 - sum_cs)
        onlyone = 0
        for child_size in cs:
            onlyone += (1 - exp_half[child_size]) * exp_half[n - 1 - child_size]
        ans += (1 - noblack - onlyone) * half
        ans %= md
    print(ans)


main()
