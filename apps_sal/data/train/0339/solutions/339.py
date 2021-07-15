class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def solve(n1s, n2s):
            answer = 0
            for num1 in n1s:
                m = collections.defaultdict(int)
                for num2 in n2s:
                    if num1**2 % num2 == 0:
                        answer += m[num1**2//num2]
                    m[num2] += 1
            return answer
        return solve(nums1, nums2)+solve(nums2,nums1)
