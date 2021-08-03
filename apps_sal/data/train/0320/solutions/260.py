class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def _op(arr):
            odds, zeros = 0, 0
            for i in range(len(arr)):
                if arr[i] == 0:
                    zeros += 1
                elif arr[i] % 2 == 1:
                    arr[i] -= 1
                    odds += 1
            if zeros == len(arr):
                return 0
            if odds != 0:
                return odds
            for i in range(len(arr)):
                arr[i] //= 2
            return 1

        ans = 0
        ops = _op(nums)
        while ops != 0:
            ans += ops
            ops = _op(nums)
        return ans
