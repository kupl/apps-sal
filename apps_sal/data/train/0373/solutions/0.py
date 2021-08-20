class Solution:

    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        v = p = 0
        (pairs, profits) = ([], [])
        while p < length:
            v = p
            while v < length - 1 and prices[v] >= prices[v + 1]:
                v += 1
            p = v + 1
            while p < length and prices[p] >= prices[p - 1]:
                p += 1
            while pairs and prices[v] < prices[pairs[-1][0]]:
                heapq.heappush(profits, prices[pairs[-1][0]] - prices[pairs[-1][1] - 1])
                pairs.pop()
            while pairs and prices[p - 1] >= prices[pairs[-1][1] - 1]:
                heapq.heappush(profits, prices[v] - prices[pairs[-1][1] - 1])
                v = pairs[-1][0]
                pairs.pop()
            pairs.append((v, p))
        while pairs:
            heapq.heappush(profits, prices[pairs[-1][0]] - prices[pairs[-1][1] - 1])
            pairs.pop()
        ans = 0
        while k != 0 and profits:
            ans += -heapq.heappop(profits)
            k -= 1
        return ans
