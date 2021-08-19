class Solution:

    def lastSubstring(self, s: str) -> str:
        start = 0
        for i in range(len(s)):
            if s[i] > s[start]:
                start = i
        candidates = set()
        length = 1
        for i in range(len(s)):
            if s[i] == s[start] and (i == 0 or s[i - 1] != s[start]):
                candidates.add(i)
        while len(candidates) > 1:
            need_remove = set()
            maxc = 'a'
            for candidate in candidates:
                end = candidate + length
                if end >= len(s):
                    need_remove.add(candidate)
                    continue
                c = s[end]
                if c > maxc:
                    maxc = c
            for candidate in candidates:
                end = candidate + length
                if end >= len(s):
                    continue
                if s[end] != maxc:
                    need_remove.add(candidate)
            if len(need_remove) >= len(candidates):
                break
            for idx in need_remove:
                candidates.discard(idx)
            length += 1
        res = ''
        for candidate in candidates:
            curt = s[candidate:]
            if curt > res:
                res = curt
        return res
