class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt = 0
        accNum = {}
        ans = 0
        accNum[0] = 1
        for x in nums:
            if x%2:
                cnt += 1
            if cnt not in accNum:
                accNum[cnt] = 1
            else:
                accNum[cnt] += 1
            if cnt-k in accNum:
                ans += accNum[cnt - k]
        return ans
