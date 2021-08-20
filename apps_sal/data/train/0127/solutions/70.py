class Solution:

    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:

        def helper(G, P, group, profit, scheme, memos):
            if scheme == len(group):
                if P <= 0 and G >= 0:
                    return 1
                return 0
            if G < 0:
                return 0
            if P < 0:
                P = 0
            if P not in memos[G][scheme]:
                added = helper(G - group[scheme], P - profit[scheme], group, profit, scheme + 1, memos)
                not_added = helper(G, P, group, profit, scheme + 1, memos)
                memos[G][scheme][P if P > 0 else 0] = added + not_added
            return memos[G][scheme][P]
        memos = [[{} for _ in group] for _ in range(G + 1)]
        return helper(G, P, group, profit, 0, memos) % (10 ** 9 + 7)
