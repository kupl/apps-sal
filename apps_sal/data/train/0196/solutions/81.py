class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        '''
        12341234
        limit of  len[] < a.length


        p[i], i

        '''
        def kaden(gen):
            ans = cur = gen[0]
            for n in gen[1:]:
                cur = n + max(0, cur)
                ans = max(ans, cur)
            return ans

        ans1 = kaden(A)
        if len(A) > 1:
            s = sum(A)
            ans2 = s + kaden([-a for a in A[1:]])
            ans3 = s + kaden([-a for a in A[:-1]])
        else:
            ans2 = ans3 = -float('inf')

        return max(ans1, ans2, ans3)
