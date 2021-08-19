class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        s = []
        evencnt = 0
        for num in nums:
            if num % 2 == 1:
                s.append(evencnt)
                evencnt = 0
            else:
                evencnt += 1
        s.append(evencnt)
        res = 0
        for i in range(len(s) - k):
            res += (s[i] + 1) * (s[i + k] + 1)
        return res
