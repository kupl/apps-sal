import heapq

def main():
    N = int(input())
    C = list(input())
    R = []
    W = []
    for i, c in enumerate(C):
        if c == 'R':
            R.append(-i)
        else:
            W.append(i)
    if len(R) == 0 or len(W) == 0:
        print((0))
        return
    heapq.heapify(R)
    heapq.heapify(W)
    ans = 0
    while True:
        max_r = -1 * heapq.heappop(R)
        min_w = heapq.heappop(W)
        if max_r < min_w:
            break
        else:
            heapq.heappush(R, -min_w)
            heapq.heappush(W, max_r)
            ans += 1
    print(ans)


def __starting_point():
    main()

__starting_point()
