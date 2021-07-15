class Solution(object):
    def flipgame(self, fronts, backs):
        same = {x for i, x in enumerate(fronts) if x == backs[i]}
        ans = float('inf')
        for x in itertools.chain(fronts, backs):
            if x not in same:
                ans = min(ans, x)

        return ans if ans != float('inf') else 0
