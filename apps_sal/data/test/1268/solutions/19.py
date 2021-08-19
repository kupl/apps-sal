import heapq


def main():
    N = int(input())
    r = sum(map(int, input().split()))
    hq = []
    for b in map(int, input().split()):
        heapq.heappush(hq, -b)
    room = heapq.heappop(hq) + heapq.heappop(hq)
    if -room >= r:
        return 'YES'
    return 'NO'


def __starting_point():
    print(main())


__starting_point()
