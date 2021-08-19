from collections import deque
import heapq


def main():
    (N, K) = map(int, input().split())
    V = list(map(int, input().split()))
    res = 0
    for pull in range(K + 1):
        push = K - pull
        if push < 0 or push > N:
            continue
        for left_push in range(push + 1):
            tmp_que = deque(V)
            tmp_heap = []
            heapq.heapify(tmp_heap)
            right_push = push - left_push
            for _ in range(left_push):
                heapq.heappush(tmp_heap, tmp_que.popleft())
            for _ in range(right_push):
                heapq.heappush(tmp_heap, tmp_que.pop())
            tmp_res = sum(tmp_que)
            for i in range(min(push, pull)):
                x = heapq.heappop(tmp_heap)
                if x >= 0:
                    heapq.heappush(tmp_heap, x)
                    break
            res = max(res, sum(tmp_heap))
    print(res)
    return


def __starting_point():
    main()


__starting_point()
