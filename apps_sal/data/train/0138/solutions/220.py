class Solution:

    def getMaxLen(self, nums: List[int]) -> int:

        def getMaxLenNonzero(arr):
            neg = []
            for (i, num) in enumerate(arr):
                if num < 0:
                    neg.append(i)
            if len(neg) % 2 == 0:
                return len(arr)
            if len(neg) == 1:
                return max(neg[0], len(arr) - neg[-1] - 1)
            return max(neg[-1], len(arr) - neg[0] - 1)
        currArr = []
        ans = 0
        for num in nums:
            if num != 0:
                currArr.append(num)
            else:
                ans = max(ans, getMaxLenNonzero(currArr))
                currArr = []
        if currArr:
            ans = max(ans, getMaxLenNonzero(currArr))
        return ans
