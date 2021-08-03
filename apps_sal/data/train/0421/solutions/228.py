class Solution:
    def lastSubstring(self, s: str) -> str:

        def find(s, candidates, step):
            if len(candidates) == 1:
                return candidates[0]
            max_char = max(s[i + step] for i in candidates if i + step < len(s))
            new_candidates = [i for i in candidates if i + step < len(s) and s[i + step] == max_char]
            return find(s, new_candidates, step + 1)

        if not s:
            return s
        if len(set(s)) == 1:
            return s

        index = find(s, list(range(len(s))), 0)
        return s[index:]
