class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        memo = [nums[0]]
        if not nums:
            return 0
        m = nums[0]
        for i in range(1, k):
            memo.append(nums[i] + max(0, m))
            if memo[-1] > m:
                m = memo[-1]
        import copy
        window = copy.deepcopy(memo)
        # m=max(window)
        for i in range(k, len(nums)):
            # print(m,memo,window)
            memo.append(nums[i] + max(0, m))
            window.append(memo[-1])
            p = window.pop(0)
            if memo[-1] > m:
                m = memo[-1]
            elif p == m:
                m = max(window)
        return max(memo)
