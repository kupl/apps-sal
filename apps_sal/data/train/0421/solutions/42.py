class Solution:
    def lastSubstring(self, s: str) -> str:

        pos = defaultdict(list)
        large = 'a'
        for i, c in enumerate(s):
            pos[c].append(i)
            large = max(large, c)

        remain = set(pos[large])
        sz = 1
        while len(remain) > 1:
            large = ''
            for idx in remain:
                if idx + sz < len(s) and s[idx + sz] > large:
                    large = s[idx + sz]

            to_remove = set()
            for idx in remain:
                if idx + sz in remain:
                    to_remove.add(idx + sz)
                if idx + sz >= len(s) or s[idx + sz] != large:
                    to_remove.add(idx)
            remain -= to_remove
            sz += 1
        idxs = [a for a in remain]
        return s[idxs[0]:]
