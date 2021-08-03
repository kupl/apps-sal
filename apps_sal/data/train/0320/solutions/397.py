class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = set(nums)
        if len(s) == 1 and 0 in s:
            return 0
        else:
            l = nums
            cnt = 0
            for i in range(len(l)):
                if l[i] % 2 == 1:
                    cnt += 1
                    l[i] -= 1
            if cnt == 0:
                return 1 + self.minOperations([a // 2 for a in l])
            else:
                return cnt + self.minOperations(l)
