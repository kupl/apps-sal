class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:

        pre_sum = [A[0]]
        for i in range(1, len(A)):
            pre_sum.append(pre_sum[-1] + A[i])

        def cal(l, r):
            if (l == 0):
                return pre_sum[r]
            else:
                return pre_sum[r] - pre_sum[l - 1]

        l = 0
        r = 0
        ans = K
        while (l < len(A)):
            #print (l,r)
            while (r < len(A) and (r - l + 1) - cal(l, r) <= K):
                ans = max(ans, r - l + 1)
                r = r + 1
            #print (r)

            if (r == len(A)):
                break

            while (l < len(A) and (r - l + 1) - cal(l, r) > K):
                l = l + 1
            #print (l)

        return ans
