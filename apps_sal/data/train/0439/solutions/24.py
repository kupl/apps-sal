class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        # https://blog.csdn.net/XX_123_1_RJ/article/details/86591150
        # https://blog.csdn.net/fuxuemingzhu/article/details/86563567
        N = len(A)
        if N == 1:
            return 1
        ans = 1
        left = 0
        right = 1
        isde = False

        while right < N:
            if A[right] == A[right - 1]:
                left = right
                right += 1
            elif (right - left == 1) or ((A[right] - A[right - 1] < 0) != isde):
                isde = A[right] - A[right - 1] < 0
                ans = max(ans, right - left + 1)
                right += 1
            else:
                left = right - 1

        return ans
