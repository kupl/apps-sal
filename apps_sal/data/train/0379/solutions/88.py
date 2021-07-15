class Solution:
    def maxSum(self, a: List[int], b: List[int]) -> int:
        a2i = {n: i for i, n in enumerate(a)}
        b2i = {n: i for i, n in enumerate(b)}
        @lru_cache(None)
        def solve(i, is_a, switched):
            if is_a:
                c = a
                c2i = a2i
                d = b
                d2i = b2i
            else:
                c = b
                c2i = b2i
                d = a
                d2i = a2i
            add = 0 if switched else c[i]
            best = add
            if not switched and c[i] in d2i:
                best = add + solve(d2i[c[i]], not is_a, True)
            if i == len(c) - 1:
                return best
            return max(best, add + solve(i + 1, is_a, False))
        return max(solve(0, True, False), solve(0, False, False)) % (10**9 + 7)
            
            
            
        

