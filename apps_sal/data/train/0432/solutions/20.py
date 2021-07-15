class Solution:
    def isPossibleDivide(self, nums, k):
        if len(nums) % k: return False
        cnt = dict()
        for v in nums:
            cnt[v] = cnt.get(v, 0) + 1
        nums.sort()
        for v in nums:
            if v not in cnt: continue
            for item in range(v, v+k):
                if item not in cnt: return False
                cnt[item] -= 1
                if cnt[item] == 0: del cnt[item]
        return True
