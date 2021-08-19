class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        ans = {}
        for i in range(len(A)):
            if A[i] in list(ans.keys()):
                ans[A[i]].append(i)
            else:
                ans[A[i]] = [i]

        B = sorted(A, reverse=True)
        # print(B)
        max_index = -1
        ramp = 0
        for key in B:

            l = max_index - ans[key][0]
            ramp = max(ramp, l)
            max_index = max(max_index, ans[key][len(ans[key]) - 1])

        return ramp
