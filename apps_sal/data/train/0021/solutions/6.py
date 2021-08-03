import sys
ints = (int(x) for x in sys.stdin.read().split())
sys.setrecursionlimit(3000)


def main():
    ntc = next(ints)
    for tc in range(1, ntc + 1):
        n = next(ints)
        s = [next(ints) for i in range(n)]
        P = None
        for x in s:
            p = set(x ^ y for y in s)
            if P == None:
                P = p
            else:
                P &= p
        ans = next(iter(sorted(P)[1:]), -1)
        print(ans)
    return


main()
