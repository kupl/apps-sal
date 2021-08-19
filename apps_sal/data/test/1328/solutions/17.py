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


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def SI():
    return sys.stdin.readline()[:-1]


def allptn(abc, ma, mb):
    inf = 10 ** 9
    allabc = [(0, 0, 0)]
    for (a, b, c) in abc:
        n = len(allabc)
        for i in range(n):
            (aa, bb, cc) = allabc[i]
            allabc.append((aa + a, bb + b, cc + c))
    vc = {}
    ans = inf
    for (a, b, c) in allabc[1:]:
        val = a * mb - b * ma
        if val:
            pc = vc.setdefault(val, inf)
            if c < pc:
                vc[val] = c
        elif c < ans:
            ans = c
    res = [(val, c) for (val, c) in sorted(vc.items())]
    return (ans, res)


def main():
    (n, ma, mb) = MI()
    abc = [LI() for _ in range(n)]
    inf = 10 ** 9
    (ans, pre) = allptn(abc[:n // 2], ma, mb)
    (ret, pos) = allptn(abc[n // 2:], ma, mb)
    ans = min(ans, ret)
    j = len(pos) - 1
    for (val, c) in pre:
        while val + pos[j][0] > 0 and j:
            j -= 1
        if val + pos[j][0] == 0:
            ans = min(ans, c + pos[j][1])
    if ans == inf:
        print(-1)
    else:
        print(ans)


main()
