class Solution:

    def lastSubstring(self, s: str) -> str:
        (n, pointer) = (len(s), 0)
        starts = list(range(n))
        while len(starts) > 1:
            max_end = max([s[start + pointer] for start in starts if start + pointer < n])
            new_starts = []
            for (i, start) in enumerate(starts):
                if i > 1 and starts[i - 1] + pointer == start:
                    continue
                elif start + pointer == n:
                    break
                if s[start + pointer] == max_end:
                    new_starts.append(start)
            pointer += 1
            starts = new_starts
        return s[starts[0]:]
