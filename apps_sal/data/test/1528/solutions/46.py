import sys
sys.setrecursionlimit(10**9)


def mi(): return map(int, input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))


INF = 10**20


def main():
    N, X = mi()

    def solve(n, x):
        # print(n,x)
        if n == 0:
            return 1
        c = 2**(n + 2) - 3
        half = c // 2

        res = 0
        if x <= half:
            if x == 1:
                res += 0
            else:
                res += solve(n - 1, x - 1)
        elif x == half + 1:
            res += 2**(n - 1 + 1) - 1 + 1
        elif x < c:
            res += 2**(n - 1 + 1) - 1 + 1 + solve(n - 1, x - (half + 1))
        else:
            assert x == c
            res += 2**(n + 1) - 1

        return res

    print(solve(N, X))


def __starting_point():
    main()


__starting_point()
