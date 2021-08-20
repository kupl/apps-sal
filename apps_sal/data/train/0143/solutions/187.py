class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        if len(tree) == 1:
            return 1
        lo = 0
        hi = 1
        baskets = set()
        baskets.add(tree[0])
        bmaps = {}
        bmaps[tree[0]] = 1
        cnt = 1
        while hi < len(tree):
            baskets.add(tree[hi])
            if tree[hi] in bmaps:
                bmaps[tree[hi]] += 1
            else:
                bmaps[tree[hi]] = 1
            while len(baskets) > 2:
                if bmaps[tree[lo]] == 1:
                    baskets.remove(tree[lo])
                    bmaps[tree[lo]] = 0
                else:
                    bmaps[tree[lo]] -= 1
                lo += 1
            cnt = max(hi - lo + 1, cnt)
            hi += 1
        return cnt
