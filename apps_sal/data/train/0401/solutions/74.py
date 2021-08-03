class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        ans = 0
        next_nums = []
        nums1, nums2 = [], []
        nums.sort(reverse=True)
        for n in nums:
            val = n % 3
            if val == 0:
                ans += n
            elif val == 1:
                nums1.append(n)
            else:
                nums2.append(n)

        if len(nums1) < len(nums2):
            small = nums1
            big = nums2
        else:
            small = nums2
            big = nums1

        mod = (len(big) - len(small)) % 3
        val1, val2 = 0, 0
        if mod == 0:
            val1 = sum(big) + sum(small)
        else:
            val1 = sum(small) + sum(big[:-mod])
            if len(big) >= 3 and 3 - mod <= len(small):
                val2 = sum(small[:-(3 - mod)]) + sum(big)

        return ans + max(val1, val2)

    def traversal(self, nums1, nums2, idx1, idx2, curr_val, visited):
        if idx1 == len(nums1) and idx2 == len(nums2):
            return curr_val, True

        if (idx1, idx2, curr_val) in visited:
            return visited[(idx1, idx2, curr_val)], False

        if idx1 + 1 <= len(nums1) and idx2 + 1 <= len(nums2):
            val, ret = self.traversal(
                nums1,
                nums2,
                idx1 + 1,
                idx2 + 1,
                curr_val + nums1[idx1] + nums2[idx2],
                visited
            )
            if ret:
                return val, True
            max_val = max(max_val, val)

        max_val = curr_val
        if idx2 + 3 <= len(nums2):
            s = nums2[idx2] + nums2[idx2 + 1] + nums2[idx2 + 2]
            val, ret = self.traversal(
                nums1,
                nums2,
                idx1,
                idx2 + 3,
                curr_val + s,
                visited
            )
            if ret:
                return val, True
            max_val = max(max_val, val)

        if idx1 + 3 <= len(nums1):
            s = nums1[idx1] + nums1[idx1 + 1] + nums1[idx1 + 2]
            val, ret = self.traversal(
                nums1,
                nums2,
                idx1 + 3,
                idx2,
                curr_val + s,
                visited
            )
            if ret:
                return val, True
            max_val = max(max_val, val)

        visited[(idx1, idx2, curr_val)] = max_val
        return max_val, True
