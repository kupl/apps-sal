class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        states = [(False, False, False, False, False)]
        seen = {}
        mapping = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

        for i in range(len(s)):
            vector = list(states[-1])
            character = s[i]

            if character in mapping:
                vector[mapping[character]] = not vector[mapping[character]]

            states.append(tuple(vector))

        res = 0

        for i, v in enumerate(states):

            if v in seen:
                res = max(res, i - seen[v])
            else:
                seen[v] = i

        return res
