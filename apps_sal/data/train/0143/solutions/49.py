class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        '''
        sliding window
        O(N)
        '''
        if len(tree) == 1:
            return 1

        l = 0
        r = 1

        curr_window = defaultdict(int)
        curr_window[tree[l]] += 1
        res = 1
        while r < len(tree):
            curr_window[tree[r]] += 1
            while len(curr_window) > 2:
                curr_window[tree[l]] -= 1
                if curr_window[tree[l]] == 0:
                    del curr_window[tree[l]]
                l += 1

            if r - l + 1 > res:
                res = r - l + 1

            r += 1

        return res
