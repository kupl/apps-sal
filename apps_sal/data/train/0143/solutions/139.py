class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        '''
        Sliding window: the window can at most only have two distinct numbers
        Find the longest sliding window
        Technique: keep the last seen index of each fruit type in my current sliding window
        seen: { x: i, y: j }
        Whenever a new type of fruit is ahead, fast forward the left boundary to min(i,j) + 1
        '''
        ans = 0
        lo, hi = -1, 0
        seen = {}
        for hi in range(len(tree)):
            if tree[hi] not in seen and len(seen) == 2:
                # tree[hi] is not in seen and seen already has 2 elements
                remove = (float('inf'), None)
                for typ in seen:
                    remove = min(remove, (seen[typ], typ))
                lo = seen.pop(remove[1])
            seen[tree[hi]] = hi
            #print(lo, hi, seen)
            ans = max(ans, hi - lo)
        return ans
