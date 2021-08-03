class Solution:
    def subarraysWithKDistinct(self, A: List[int], k: int) -> int:
        dic = {}
        n = len(A)
        left = 0
        right = 0
        cnt = 0
        for i in range(n):
            if A[i] in dic:
                dic[A[i]] += 1
            else:
                dic[A[i]] = 1
            l = len(dic)
            if l == k + 1:
                del dic[A[right]]
                right += 1
                left = right
                l -= 1
            if l == k:
                while dic[A[right]] > 1:
                    dic[A[right]] -= 1
                    right += 1
                cnt += right - left + 1
        return cnt
