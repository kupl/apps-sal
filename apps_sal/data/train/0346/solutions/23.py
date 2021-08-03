class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt = 0
        d = {}
        d[0] = 1
        for i in nums:
            if i % 2:
                cnt += 1
            if cnt in d:
                d[cnt] += 1
            else:
                d[cnt] = 1

        ans = 0
        for key in d:
            if k + key in d:
                ans += (d[key] * d[k + key])
        return ans
