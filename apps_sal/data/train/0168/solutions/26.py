class Solution:

    def canConstruct(self, s: str, k: int) -> bool:
        cnt_map = collections.defaultdict(int)
        for c in s:
            cnt_map[c] += 1
        n_odd = 0
        for c in cnt_map:
            if cnt_map[c] % 2 == 1:
                n_odd += 1
        if n_odd <= k <= len(s):
            return True
        else:
            return False
