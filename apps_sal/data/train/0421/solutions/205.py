class Solution:
    def lastSubstring(self, s: str) -> str:

        # naive: O(n^2)
        # slight optimization to sort as we go
        #         last = s
        #         for i in range(len(s)):
        #             for j in range(i+1, len(s)+1):
        #                 if s[i:j] > last:
        #                     last = s[i:j]

        #         return last

        # find positions of earliest letters in alphabet
        # leastLetter = s[0]
        # positions = [0]
        # for i in range(1,len(s)):
        #     if s[i] > leastLetter:
        #         leastLetter = s[i]
        #         positions = [i]
        #     elif s[i] == leastLetter:
        #         positions.append(i)
        i, j, k = 0, 1, 0
        n = len(s)
        while j + k < n:
            if s[i + k] == s[j + k]:
                k += 1
                continue
            elif s[i + k] > s[j + k]:
                j = j + k + 1
            else:
                i = i + k + 1
            if i == j:
                j = j + 1
            k = 0
        return s[i:]
