class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        ans = 0
        l = 0
        r = 0
        prefix = [0 for i in range(len(A))]
        for i in range(len(A)):
            if (i == 0):
                prefix[i] = A[0]
            else:
                prefix[i] = A[i] + prefix[i - 1]

        if (K >= len(A) - prefix[-1]):
            return len(A)

        while (r < len(A) and l < len(A)):
            while (r < len(A)):
                if (l == 0):
                    this_sum = prefix[r]
                else:
                    this_sum = prefix[r] - prefix[l - 1]

                if (r - l + 1 - this_sum > K):
                    r -= 1
                    break

                r += 1

            if (r >= len(A)):
                if (r - l > ans):
                    ans = r - l
                break

            if (r - l + 1 > ans):
                ans = r - l + 1

            while (l < len(A) and A[l] == 1):
                l += 1

            l += 1

        return ans
