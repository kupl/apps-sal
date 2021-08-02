import sys
sys.setrecursionlimit(10**9)


def mi(): return map(int, input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))


INF = 10**20


def main():
    A, B, K = mi()
    ans = set()
    for i in range(A, A + K):
        if A <= i <= B:
            ans.add(i)

    for i in range(B - K + 1, B + 1):
        if A <= i <= B:
            ans.add(i)

    ans = list(ans)
    ans.sort()
    print(*ans, sep='\n')


def __starting_point():
    main()


__starting_point()
