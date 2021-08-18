class Solution:
    def lastSubstring(self, s: str) -> str:

        n = len(s)
        offset = 0
        cand_starts = list(range(len(s)))

        while len(cand_starts) > 1:
            max_end = 'a'

            for start in cand_starts:
                if start + offset < n:
                    max_end = max(max_end, s[start + offset])

            new_starts = []

            for idx, start in enumerate(cand_starts):
                if 1 < idx and cand_starts[idx - 1] + offset == start:
                    continue

                if start + offset == n:
                    break

                if s[start + offset] == max_end:
                    new_starts.append(start)

            cand_starts = new_starts
            offset += 1

        return s[cand_starts[0]:]
