import heapq


def abc151d_maze_master():
    (h, w) = map(int, input().split())
    s = []
    max_val = 0
    for i in range(h):
        s.append(input())
    for hi in range(h):
        for wi in range(w):
            if s[hi][wi] == '#':
                continue
            flg = [[-1] * w for _ in range(h)]
            flg[hi][wi] = 0
            q = [(0, hi, wi)]
            heapq.heapify(q)
            while len(q) > 0:
                (d, hj, wj) = heapq.heappop(q)
                for (dh, dw) in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                    if 0 <= hj + dh < h and 0 <= wj + dw < w and (s[hj + dh][wj + dw] != '#') and (flg[hj + dh][wj + dw] == -1 or flg[hj + dh][wj + dw] > flg[hj][wj] + 1):
                        heapq.heappush(q, (d + 1, hj + dh, wj + dw))
                        flg[hj + dh][wj + dw] = flg[hj][wj] + 1
            max_val = max(max_val, max([max(v) for v in flg]))
    print(max_val)


abc151d_maze_master()
