import sys
sys.setrecursionlimit(10**7)


def main():
    N, M = list(map(int, input().split()))
    l = [[] for _ in range(N)]
    for _ in range(M):
        a, b = list(map(int, input().split()))
        l[a - 1].append(b - 1)
    c = [0] * N
    loop = []

    def cyclic(n):
        if c[n] == 2:
            return False
        if c[n] == 1:
            loop.append(n)
            return True
        c[n] = 1
        for i in l[n]:
            if cyclic(i):
                loop.append(n)
                return True
        c[n] = 2
        return False
    for i in range(N):
        if cyclic(i):
            break
    if len(loop) == 0:
        print((-1))
        return
    loop.reverse()
    t = loop[-1]
    loop = loop[loop.index(t):]
    ll = set(loop)
    flag = True
    while flag:
        for i, v in enumerate(loop[:-1]):
            flag2 = False
            for j in l[v]:
                if j in ll and loop[i + 1] != j:
                    if loop.index(j) == 0:
                        loop = loop[:i + 1] + [j]
                    elif loop.index(j) < i:
                        loop = loop[loop.index(j):i + 1] + [j]
                    else:
                        loop = loop[:i + 1] + loop[loop.index(j):]
                    ll = set(loop)
                    flag2 = True
                    break
            if flag2:
                break
        else:
            flag = False
    loop = set(loop)
    print((len(loop)))
    for i in loop:
        print((i + 1))
    return


main()
