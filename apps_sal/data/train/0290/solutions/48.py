class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        #         cuts = sorted(cuts)
        #         options = []
        #         cuts = [0]+cuts+[n]
        #         N = len(cuts)
        #         for i in range(1, N):
        #             options.append([cuts[i-1], cuts[i]])

        #         val = 0
        #         while len(options) != 1:
        #             short_i = 0
        #             min_wid = math.inf
        #             for i in range(len(options)-1):
        #                 a = options[i]
        #                 b = options[i+1]
        #                 if (a[1]-a[0]) + (b[1]-b[0]) < min_wid:
        #                     short_i = i
        #                     min_wid = (a[1]-a[0]) + (b[1]-b[0])

        #             val += min_wid
        #             options[short_i][1] = options[short_i+1][1]
        #             del options[short_i+1]

        #         return val

        cuts = sorted(cuts)
        memo = {}
        t_cuts = [0] + cuts + [n]
        N = len(t_cuts)
        for i in range(1, N):
            memo[(t_cuts[i - 1], t_cuts[i])] = 0

        def dp(s, e):
            # print((s,e), memo[(s,e)] if (s,e) in memo else False)
            if (s, e) in memo:
                return memo[(s, e)]

            filtered_cuts = [cut for cut in cuts if cut > s and cut < e]
            if len(filtered_cuts) == 0:
                return 0

            ans = math.inf
            for cut in filtered_cuts:
                ans = min(ans, (e - s) + dp(s, cut) + dp(cut, e))

            memo[(s, e)] = ans
            return memo[(s, e)]

        ans = dp(0, n)
        # print(memo)
        return ans
