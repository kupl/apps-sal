class Solution:
    def numSplits(self, s: str) -> int:
        s_cnt = Counter(s)
        p_cnt = defaultdict(int)
        count = 0
        for ch in s:
            p_cnt[ch] += 1
            s_cnt[ch] -= 1
            if s_cnt[ch] == 0: del(s_cnt[ch])
            if len(s_cnt.keys()) == len(p_cnt.keys()): count += 1
        return count
