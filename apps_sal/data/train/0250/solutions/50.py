class Solution:

    def mincostToHireWorkers(self, quality, wage, K):
        workers = sorted(([float(w) / q, q] for (w, q) in zip(wage, quality)))
        res = float('inf')
        qsum = 0
        heap = []

        def rec(l, r, heap, newQ):
            if l > r:
                heap.insert(l, newQ)
                return heap
            m = l + int((r - l) / 2)
            if heap[m] > newQ:
                return rec(l, m - 1, heap, newQ)
            else:
                return rec(m + 1, r, heap, newQ)
        L = 0
        for (r, q) in workers:
            heap = rec(0, L - 1, heap, q)
            L += 1
            qsum += q
            if L > K:
                p = heap.pop(K)
                L -= 1
                qsum += -p
            if len(heap) == K:
                res = min(res, qsum * r)
        return res
