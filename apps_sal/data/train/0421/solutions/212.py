class Solution:
    def lastSubstring(self, s: str) -> str:

        # Recursively find all with the largest lecsographical order,

        # when only one left => that is end of our substring

        # store start index and end index
        all_same = True
        first_char = s[0]
        for c in s:
            if first_char != c:
                all_same = False
        if all_same:
            return s

        max_char = max([c for c in s])
        indexes = [[i, i + 1] for i, c in enumerate(s) if c == max_char]

        output = []

        def max_substring(indexes):
            if len(indexes) == 1:
                output.append(indexes[0])
                return

            nonlocal s
            max_char = max([s[indx[1]] for indx in indexes if indx[1] < len(s)])

            next_indexes = []
            for indx in indexes:
                if indx[1] < len(s) and s[indx[1]] == max_char:
                    indx[1] += 1
                    next_indexes.append(indx)
            max_substring(next_indexes)

        max_substring(indexes)
        return s[output[0][0]:]
