class Solution:
    """
    https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/discuss/830480/C%2B%2B-O(N)-Sliding-window-Explanation-with-Illustrations
    1,2,3,10,4,2,3,5]
    1 2 2  3 3 4 5 10
    """

    def findLengthOfShortestSubarray(self, A: List[int]) -> int:
        N = len(A)
        (left, right) = (0, N - 1)
        while left + 1 < N and A[left] <= A[left + 1]:
            left += 1
        if left == N - 1:
            return 0
        while right > left and A[right - 1] <= A[right]:
            right -= 1
        ans = min(N - left - 1, right)
        (i, j) = (0, right)
        while i <= left and j < N:
            if A[j] >= A[i]:
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1
        return ans
