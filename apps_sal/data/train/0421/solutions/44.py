class Solution:
    def lastSubstring(self, s: str) -> str:
        n, offset = len(s), 0
        starts = list(range(n))
        while len(starts) > 1:
            max_end = max(s[start + offset] for start in starts if start + offset < n)
            new_starts = []
            for i, start in enumerate(starts):
                if i > 1 and starts[i - 1] + offset == start: continue
                if start + offset == n: break
                if s[start + offset] == max_end: new_starts += start,
            offset += 1
            starts = new_starts
        return s[starts[0]:]
