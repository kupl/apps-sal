import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


def main():
    (n, m) = map(int, input().split())
    li = []
    for _ in range(n):
        (b, a) = map(int, input().split())
        if m - b >= 0:
            li.append([a, m - b])
    li.sort(key=lambda x: x[1])
    h = []
    for i in li:
        if len(h) >= i[1] + 1:
            heapq.heappushpop(h, i[0])
        else:
            heapq.heappush(h, i[0])
    print(sum(h))


def __starting_point():
    main()


__starting_point()
