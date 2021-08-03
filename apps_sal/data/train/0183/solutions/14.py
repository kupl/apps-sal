class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        max_dot_product = [nums1[0] * num for num in nums2]
        max_dot_product = list(itertools.accumulate(max_dot_product, max))
        for num1 in nums1[1:]:
            max_dot_product_next = []
            for i, num2 in enumerate(nums2):
                curr_max = max_dot_product[i]
                if i > 0:
                    curr_max = max(curr_max, max(num1 * num2 + max_dot_product[i - 1], max_dot_product_next[i - 1]))
                curr_max = max(curr_max, num1 * num2)
                max_dot_product_next.append(curr_max)
            max_dot_product = max_dot_product_next
            #print(num1, max_dot_product)
        # print(max_dot_product)
        return max(max_dot_product)
