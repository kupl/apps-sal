class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        #         for total length, find the location closest to center and cut it
        #         remove that location from cuts and move on to the parts
        #         sort the cuts array, easy to find mid that way

        #         cuts.sort()
        #         def cut(start, end, cuts, cuts_start, cuts_end):
        #             print(start, end, cuts_start, cuts_end)
        #             if end <= start or cuts_start > cuts_end:
        #                 return 0

        #             mid = (start + end) // 2
        #             loc = bisect.bisect_left(cuts, mid, cuts_start, cuts_end)

        #             print('loc', loc)
        #             if loc >= len(cuts):
        #                 return 0

        #             left = cut(start, cuts[loc], cuts, cuts_start, loc - 1)
        #             right = cut(cuts[loc], end, cuts, loc + 1, cuts_end)
        #             print('price',(end - start), left , right)
        #             v =  (end - start) + left + right
        #             return v

        #         print(cuts)
        #         return cut(0, n, cuts, 0, len(cuts))
        # TLE
        #         def top_down(low, high, cuts):
        #             possible_cuts = [c for c in cuts if low < c < high]
        #             # print(possible_cuts)
        #             if not possible_cuts:
        #                 return 0
        #             ans = float('inf')
        #             for mid in possible_cuts:
        #                 ans = min(ans, top_down(low, mid, cuts) + top_down(mid, high, cuts))
        #             return ans + high - low

        #         return top_down(0, n, cuts)
        dp = {}

        def top_down(low, high, cuts):
            if (low, high) in dp:
                return dp[(low, high)]

            possible_cuts = [c for c in cuts if low < c < high]
            # print(possible_cuts)
            if not possible_cuts:
                return 0
            ans = float('inf')
            for mid in possible_cuts:
                ans = min(ans, top_down(low, mid, cuts) + top_down(mid, high, cuts))
            dp[(low, high)] = ans + high - low
            return dp[(low, high)]

        return top_down(0, n, cuts)
