class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        """
1- expect[i] = wage[i]/quality[i]: meaning i-th worker claims expect[i] money per each unit of its quality. Therefore, if expect[i] > expect[j], that means if we pay j-th worker quality[j]*expect[i] he/she would be more than happy and it's more than its minimal requested wage.

2- Therefore, for k workers sorted by their expect values, if we pay each worker q[i]*expect[k], both rules are satisfied. The total needed money = (sum(q_1 + q_2 + ... + q_k) * expect[k]). Note that this is the minimum money for this k workers, since you have to pay the k-th worker at least q[k]*expect[k]. This part is very tricky, think of this in contrary, if you don't pay each of K workers with expected[k], let's say if you pick expected[k-1], you will not satisfy kth worker. So, the minimum expected pay per quality is expected[k] to satisfy all k workers. Every worker is paid in terms of quality ratio so we come up with a common pay per quality. 

3- To recap, we sort workers based on their expect values. Say we are at worker i and want to form a k-group and we already know it would cost sum*expect[i]. To pay the minimum money we should minimize the sum, which can be found using a maxHeap (to replace the max value with a smaller one) to keep the smaller q's as we move forward.

        """
        workers = sorted(([float(w) / q, q] for (w, q) in zip(wage, quality)))
        maxHeap = []
        res = float('inf')
        qsum = 0
        for (expect, q) in workers:
            qsum += q
            heapq.heappush(maxHeap, -q)
            if len(maxHeap) > K:
                qsum += heapq.heappop(maxHeap)
            if len(maxHeap) == K:
                res = min(res, expect * qsum)
        return res
