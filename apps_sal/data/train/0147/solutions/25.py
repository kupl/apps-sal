class Solution(object):

    def maxPerformance(self, n, speed, efficiency, k):
        worker = []
        for i in range(n):
            worker.append([speed[i], efficiency[i]])
        worker = sorted(worker, key=lambda x: x[1], reverse=True)
        print(worker)
        import heapq
        total = 0
        heap = []
        res = 0
        for i in range(k):
            total += worker[i][0]
            minE = worker[i][1]
            heapq.heappush(heap, worker[i][0])
            res = max(res, total * minE)
        for i in range(k, n):
            if worker[i][0] > heap[0]:
                total += -heap[0] + worker[i][0]
                minE = worker[i][1]
                res = max(res, minE * total)
                heapq.heappop(heap)
                heapq.heappush(heap, worker[i][0])
        return res % 1000000007

    def cmp(self, w1, w2):
        if w1[1] > w2[1]:
            return -1
        elif w1[1] == w2[1]:
            return 0
        else:
            return 1
