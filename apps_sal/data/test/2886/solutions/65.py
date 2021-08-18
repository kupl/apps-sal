
import sys


def main():
    mod = 1000000007
    inf = float('inf')
    sys.setrecursionlimit(10**6)
    def input(): return sys.stdin.readline().rstrip()
    def ii(): return int(input())
    def mi(): return list(map(int, input().split()))
    def mi_0(): return [int(x) - 1 for x in input().split()]
    def lmi(): return list(map(int, input().split()))
    def lmi_0(): return list([int(x) - 1 for x in input().split()])
    def li(): return list(input())

    def calc_consective(s):
        n = len(s)
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                return [i + 1, i + 2]
        return None

    def calc_skip(s):
        n = len(s)
        for i in range(n - 2):
            if s[i] == s[i + 2]:
                return [i + 1, i + 3]
        return None

    def calc_ans(s):
        ans = calc_consective(s)
        if ans:
            return ans
        ans = calc_skip(s)
        if ans:
            return ans
        return (-1, -1)

    s = input()
    res = calc_ans(s)
    print(("{} {}".format(res[0], res[1])))


def __starting_point():
    main()


__starting_point()
