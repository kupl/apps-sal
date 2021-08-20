class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        neighbor = dict()
        for (i, cut) in enumerate(cuts):
            if i == 0:
                neighbor[cut] = [None, cuts[i + 1]]
            elif i == len(cuts) - 1:
                neighbor[cut] = [cuts[i - 1], None]
            else:
                neighbor[cut] = [cuts[i - 1], cuts[i + 1]]
        cache = dict()

        def search(left: int, right: int) -> int:
            if (left, right) in cache:
                return cache[left, right]
            min_cost = None
            for cut in cuts:
                if cut <= left or cut >= right:
                    continue
                (leftnei, rightnei) = neighbor[cut]
                cost = right - left
                cost += search(left, cut)
                cost += search(cut, right)
                min_cost = cost if min_cost is None else min(min_cost, cost)
            if min_cost is None:
                min_cost = 0
            cache[left, right] = min_cost
            return min_cost
        ans = search(0, n)
        return ans
