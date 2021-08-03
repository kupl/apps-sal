import sys
import heapq
import math
def input(): return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    def is_good(mid, key):
        kk = 0
        for a in A:
            kk += -(-a // mid) - 1
        if kk <= key:
            return True
        else:
            return False

    def bi_search(bad, good, key):
        while good - bad > 1:
            mid = (bad + good) // 2
            if is_good(mid, key):
                good = mid
            else:
                bad = mid
        return good

    print(bi_search(0, 1000000000, k))


def __starting_point():
    main()


__starting_point()
