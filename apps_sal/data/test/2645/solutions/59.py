
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

    s = input()
    n = len(s)
    par_counter = s.count('p')
    print((n // 2 - par_counter))


def __starting_point():
    main()


__starting_point()
