class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        cache = {}
        def helper(remaining):
            if remaining == 0:
                return ''
            if remaining in cache:
                return cache[remaining]
            maximum = '0'
            for i in range(len(cost)):
                if cost[i] > remaining:
                    continue
                result = helper(remaining - cost[i])
                if result == '0':
                    continue
                maximum = larger(maximum, str(i+1) + result)
            cache[remaining] = maximum
            return maximum

        def larger(a, b):
            if len(a) > len(b):
                return a
            if len(a) < len(b):
                return b
            return max(a, b)

        return helper(target)
