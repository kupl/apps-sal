class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        left = [A[0], ]
        right = [A[-1], ]
        for i in range(1, len(A)):
            left.append(min(A[i], left[i - 1]))
            right.append(max(A[len(A) - 1 - i], right[-1]))
        right = right[::-1]
        pt_l = 0
        pt_r = 0
        ans = 0
        while pt_r < len(A):
            if left[pt_l] <= right[pt_r]:
                ans = max(ans, pt_r - pt_l)
                pt_r += 1
            else:
                pt_l += 1
        return ans
