class Solution(object):

    def mincostToHireWorkers(self, quality, wage, K):
        from fractions import Fraction
        workers = sorted((Fraction(w, q), q, w)
                         for q, w in zip(quality, wage))

        ans = float('inf')
        pool = []
        sumq = 0
        for ratio, q, w in workers:
            heapq.heappush(pool, -q)
            sumq += q

            if len(pool) > K:
                sumq += heapq.heappop(pool)

            if len(pool) == K:
                ans = min(ans, ratio * sumq)

        return float(ans)


# Idea is as follows: If workers are paid in ratio of their qualities, then w_j = (w_ref/q_ref) * q_j

# After paying in the above ratio, to ensure we pay workers their min wage, then we need to select the higher wage/ratio as reference among two possible wage/quality ratios


# So if the size of array is k, then we just select the highest ratio and use that as ref, then
#  min cost =  (highest ratio ) * (sum of all Qualities)

# or in other words, sort the wage to ratios in increasing order, then last one will be ref ration and this ref ratio times sumq = ans.

# now consider k+1 elements present. then same as above logic, if we sort the wage/quality ratios in increasing order, then any of the ratios from kth to later can be a candidate ref ratio. If k elements, we already know the ans is kth ratio * sumq. Now consider k+1 th element. We can have this as ref ration instead. Then which one would we remove to get k elements? We want to remove the element with highest quality as that would reduce the cost by max. (remember total cost = ref ratio * ( sum of qualities)). So we use max heap to maintain qualities and remove the highest quality when we consider all indexes > k. and among all those possible indexes k to n, we find which gives min cost.
