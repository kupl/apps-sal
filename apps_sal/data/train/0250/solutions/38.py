class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        # length = len(quality)
        # value_orders = sorted(range(length), key=lambda k: wage[k] / quality[k])

        # worker_quality = []
        # minimum_cost = 0
        # for i in range(0, K):
        #     worker_quality.append(quality[value_orders[i]])
        #     minimum_cost += wage[value_orders[K - 1]] / quality[value_orders[K - 1]] * quality[value_orders[i]]

        # worker_quality.sort()
        # for i in range(K, length):
        #     if quality[value_orders[i]] < worker_quality[-1]:
        #         worker_quality.pop()
        #         worker_quality.append(quality[value_orders[i]])
        #         worker_quality.sort()
        #     this_round_cost = 0
        #     for q in worker_quality:
        #         this_round_cost += q * wage[value_orders[i]] / quality[value_orders[i]]
        #     minimum_cost = min(minimum_cost, this_round_cost)
        # return minimum_cost

        workers = [(wage / quality, wage, quality) for wage, quality in zip(wage, quality)]
        workers.sort(key=lambda x: x[0])

        heap = []
        quality_sum = 0
        final_cost = float('inf')

        for ratio, wage, quality in workers:
            heapq.heappush(heap, -1 * quality)
            quality_sum += quality

            if len(heap) > K:
                q = heapq.heappop(heap)
                # adding rather than substracting, since quality is inserted as negative
                quality_sum += q

            if len(heap) == K:
                cost = ratio * quality_sum
                final_cost = min(final_cost, cost)
        return final_cost
