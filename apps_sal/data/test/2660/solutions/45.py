import heapq
import sys
input = sys.stdin.readline


def main():
    less = []
    greater = []
    s = 0
    sum_ = 0
    q = int(input())

    def query(n):
        nonlocal s, sum_
        if n[0] == "1":
            c, a, b = map(int, n.split())
            s += b
            if len(less) == len(greater):
                if not greater or a <= greater[0]:
                    heapq.heappush(less, -a)
                    sum_ -= a
                else:
                    r = heapq.heappushpop(greater, a)
                    heapq.heappush(less, -r)
                    sum_ += a - 2 * r
            else:
                if a >= -less[0]:
                    heapq.heappush(greater, a)
                    sum_ += a
                else:
                    r = -heapq.heappushpop(less, -a)
                    heapq.heappush(greater, r)
                    sum_ += 2 * r - a
        else:
            res = sum_
            if len(less) > len(greater):
                res -= less[0]
            res += s
            print(-less[0], res)

    for _ in range(q):
        k = input()
        query(k)


def __starting_point():
    main()


__starting_point()
