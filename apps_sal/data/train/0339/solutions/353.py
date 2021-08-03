class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_cnt = collections.Counter(nums1)
        nums1_square_cnt = {x * x: nums1_cnt[x] for x in nums1_cnt}
        nums2_cnt = collections.Counter(nums2)
        nums2_square_cnt = {y * y: nums2_cnt[y] for y in nums2_cnt}

        def f(nums_a, cnt_a, cnt_b_squares):
            uniq_a_vals = list(cnt_a.keys())
            if len(uniq_a_vals) == 1:
                x = uniq_a_vals[0]
                if x * x in cnt_b_squares:
                    return (cnt_a[x] * (cnt_a[x] - 1) // 2) * cnt_b_squares[x * x]

            total = 0
            for i in range(len(nums_a)):
                for j in range(i + 1, len(nums_a)):
                    x, y = nums_a[i], nums_a[j]
                    if x * y in cnt_b_squares:
                        total += cnt_b_squares[x * y]
            return total

        return f(nums1, nums1_cnt, nums2_square_cnt) + f(nums2, nums2_cnt, nums1_square_cnt)
