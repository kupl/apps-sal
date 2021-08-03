class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        subarrays = []
        temp = []
        for i in range(len(nums)):
            if nums[i] == 0:
                subarrays.append(temp.copy())
                temp = []
            else:
                temp += [nums[i]]
        subarrays.append(temp.copy())

        def util(a):
            p = 1
            for i in a:
                p *= i
            if p > 0:
                return len(a)
            else:
                i = 0
                while a[i] > 0:
                    i += 1
                ans1 = len(a) - i - 1
                j = len(a) - 1
                while a[j] > 0:
                    j -= 1
                ans2 = j
                return max(ans1, ans2)
        maxm = -1
        for i in subarrays:
            maxm = max(maxm, util(i))
        return maxm
