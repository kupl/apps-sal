class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        target = []
        t = []
        for n in nums:
            if n != 0:
                t.append(n)
            else:
                target.append(t.copy())
                t = []
        target.append(t.copy())

        def find(nums):
            if len(nums) == 0:
                return 0
            positive_ma = -1
            positive_min = -1
            negtive_ma = -1
            negtive_mi = -1
            t = 1
            for i in range(len(nums)):
                t *= nums[i]
                if t > 0 and positive_min == -1:
                    positive_ma = i
                    positive_min = i
                elif t > 0 and positive_min != -1:
                    positive_ma = i

                if t < 0 and negtive_mi == -1:
                    negtive_mi = i
                    negtive_ma = i
                elif t < 0 and negtive_mi != -1:
                    negtive_ma = i

            p_l = 0
            n_l = 0
            if positive_min != -1:
                p_l = positive_ma + 1

            if negtive_mi != -1 and negtive_mi != negtive_ma:
                n_l = negtive_ma - negtive_mi
            print((positive_ma, positive_min, negtive_ma, negtive_mi))
            return max(p_l, n_l)

        result = 0
        for t in target:

            result = max(result, find(t))
        return result
