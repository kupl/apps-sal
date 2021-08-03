class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def count(num):
            div = 0
            minus = 0
            while num:
                if num % 2 == 0:
                    num = num // 2
                    div += 1
                else:
                    num = num - 1
                    minus += 1
            return div, minus
        m = []
        d = []
        for i in nums:
            div, minus = count(i)
            d.append(div)
            m.append(minus)
        return max(d) + sum(m)
