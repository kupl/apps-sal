import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    h, n = map(int, input().split())
    ab = [list(map(int, input().split())) for i in range(n)]
    ans = [0] * (4 * 10**4)
    for i in range(1, h + 1):
        li = [ans[i - j[0]] + j[1] for j in ab]
        ans[i] = min(li)
    print(ans[h])


def __starting_point():
    main()


__starting_point()
