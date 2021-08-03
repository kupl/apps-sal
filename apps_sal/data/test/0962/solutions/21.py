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
    print((0))
    return


main()
