class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        queue = []
        i = ans = 0
        for j in range(len(A)):
            if A[j] != 1:
                if len(queue) == K:
                    try:
                        i = queue.pop(0) + 1
                    except:
                        i = j + 1
                if len(queue) < K:
                    queue.append(j)
            ans = max(ans, j - i + 1)
        return ans
