class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        h = {}
        heap = []
        for i in range(lo, hi + 1):
            print(i)
            q = deque()
            q.append((0, i))
            while q:
                x = q.popleft()
                if x[1] == 1 or x[1] in h:
                    # print(i,x)
                    xx = x[0]
                    if x[1] in h:
                        xx += h[x[1]]
                        # print(xx)
                    if i not in h:
                        h[i] = xx
                    if len(heap) < k:
                        heapq.heappush(heap, (-xx, -i))
                    else:
                        if -xx > heap[0][0]:
                            heapq.heappop(heap)
                            heapq.heappush(heap, (-xx, -i))
                    break
                if x[1] % 2 == 0:
                    q.append((x[0] + 1, x[1] // 2))
                else:
                    q.append((x[0] + 1, (3 * x[1]) + 1))
        # print(heap)
        return -heap[0][1]
