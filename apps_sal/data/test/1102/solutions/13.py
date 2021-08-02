from collections import defaultdict, deque, Counter, OrderedDict
import sys
sys.setrecursionlimit(20000)


def main():
    n, he = map(int, input().split())
    he -= 1
    l = [int(i) for i in input().split()]
    ans = l[he]
    for i in range(1, 100):
        tor = he + i
        tol = he - i
        if tor < n and tol >= 0:
            if l[tor] == 1 and l[tol] == 1:
                ans += 2
        elif tor < n:
            if l[tor] == 1:
                ans += 1
        elif tol >= 0:
            if l[tol] == 1:
                ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
