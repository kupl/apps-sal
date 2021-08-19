import sys
ints = (int(x) for x in sys.stdin.read().split())
sys.setrecursionlimit(3000)


def main():
    ntc = next(ints)
    for tc in range(1, ntc + 1):
        n = next(ints)
        b = [int(x) for x in bin(n)[2:]]
        k = len(b)
        ans = 0
        for i in range(k):
            if b[i]:
                ans += 2 ** (k - i) - 1
        print(ans)
    return


main()
