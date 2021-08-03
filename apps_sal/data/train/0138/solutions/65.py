class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        ans = float('-inf')
        while i < n:
            s = i

            while s < n and nums[s] == 0:
                s += 1
            e = s
            c = 0
            sn = -1
            en = -1
            while e < n and nums[e] != 0:
                if nums[e] < 0:
                    c += 1
                    if sn == -1:
                        sn = e
                    en = e
                e += 1
            if c % 2 == 0:
                ans = max(ans, e - s)
            else:
                if sn != -1:
                    ans = max(ans, e - sn - 1)
                if en != -1:
                    ans = max(ans, en - s)
            i = e + 1
        return ans
