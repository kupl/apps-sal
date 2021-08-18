
class Solution:
    def minSubarray(self, nums, p):
        total = sum(nums)
        need = total % p
        if need == 0:
            return 0

        prefix = []
        for i, n in enumerate(nums):
            if i == 0:
                prefix.append(n % p)
            else:
                prefix.append((prefix[-1] + n) % p)

        ans = len(nums)
        seen = {0: -1}
        for i, v in enumerate(prefix):
            req = (v - need) % p
            if req in seen:
                ans = min(ans, i - seen[req])
            seen[v] = i
        if ans == len(nums):
            return -1

        return ans
