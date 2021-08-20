class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        from collections import defaultdict
        nums1 = []
        for i in nums:
            if i > 0:
                nums1.append(1)
            elif i < 0:
                nums1.append(-1)
            else:
                nums1.append(0)
        pre_arr = [0] * len(nums1)
        rem = []
        for i in range(len(nums1)):
            if i == 0:
                pre_arr[i] = nums1[i]
            elif pre_arr[i - 1] != 0:
                pre_arr[i] = nums1[i] * pre_arr[i - 1]
            else:
                pre_arr[i] = nums1[i]
        a1 = max(nums)
        if a1 > 0:
            m1 = 1
        else:
            m1 = 0
        Dict = defaultdict(int)
        start = 0
        for i in range(len(pre_arr)):
            if pre_arr[i] > 0:
                m1 = max(m1, i - Dict[1] + 1)
            elif pre_arr[i] == 0:
                Dict[1] = i + 1
        Dict1 = defaultdict(list)
        m2 = 0
        for i in range(len(pre_arr)):
            if pre_arr[i] < 0:
                Dict1[-1].append(i)
            elif pre_arr[i] == 0:
                if len(Dict1[-1]) >= 2:
                    m2 = max(m2, Dict1[-1][-1] - Dict1[-1][0])
                Dict1.clear()
        if len(Dict1[-1]) >= 2:
            m2 = max(m2, Dict1[-1][-1] - Dict1[-1][0])
        return max(m1, m2)
