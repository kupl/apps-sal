import bisect


class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        ans = countzeroes = 0
        counter = {0: -1}
        for i in range(len(A)):
            num = A[i]
            if num == 0:
                countzeroes += 1
            if countzeroes not in counter:
                counter[countzeroes] = i
            j = counter[max(0, countzeroes - K)]
            ans = max(ans, i - j)
        return ans
