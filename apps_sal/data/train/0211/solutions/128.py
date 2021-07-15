class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        max_length = 1

        for code in range(2 ** (len(s) - 1)):
            subs = set()

            cur = s[0]

            for i in range(1, len(s)):
                if code % 2 == 1:
                    if cur in subs:
                        break
                    subs.add(cur)
                    cur = s[i]
                else:
                    cur += s[i]
                code = code >> 1
            if cur not in subs:
                max_length = max(max_length, len(subs) + 1)
        return max_length
