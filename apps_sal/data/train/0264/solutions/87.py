class Solution:
    def maxLength(self, arr: List[str]) -> int:
        newarr = []
        for w in arr:
            if len(set(w)) == len(w):
                newarr.append(w)
        arr = newarr
        n = len(arr)
        res = 0

        str_masks = [None] * n
        for i in range(n):
            wd = arr[i]
            mask = 0
            for ch in wd:
                ch_pos = ord(ch) - ord('a')
                mask |= 1 << ch_pos
            str_masks[i] = mask

        def dfs(idx, mask, curlen):
            nonlocal res
            if idx == n:
                res = max(res, curlen)
                return
            # use arr[idx]
            if mask & str_masks[idx] == 0:
                # can use arr[idx]
                dfs(idx + 1, mask | str_masks[idx], curlen + len(arr[idx]))
            # not use arr[idx]
            dfs(idx + 1, mask, curlen)
        dfs(0, 0, 0)
        return res
