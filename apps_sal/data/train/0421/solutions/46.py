class Solution:
    def lastSubstring(self, s: str) -> str:
        # Create a suffix array, and sort it to fetch the biggest one
        #         suffix_array = []

        #         for idx in range(len(s)):
        #             suffix_array.append(s[idx:])

        #         suffix_array.sort()

        #         return suffix_array[-1]
        # O(n^2)

        n = len(s)
        starts = list(range(n))
        offset = 0

        while len(starts) > 1:
            max_end = max(s[start + offset] for start in starts if start + offset < n)
            new_starts = []
            for idx, start in enumerate(starts):
                if idx > 1 and starts[idx - 1] + offset == start:
                    # swallow
                    continue
                if start + offset == n:
                    # end of s
                    break
                if s[start + offset] == max_end:
                    new_starts.append(start)
            offset += 1
            starts = new_starts
        return s[starts[0]:]
