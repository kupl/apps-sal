class Solution:

    def numSplits(self, s: str) -> int:
        l_count = []
        r_count = []
        tmp = 0
        for i in range(len(s)):
            if s[i] not in s[:i]:
                tmp += 1
            l_count.append(tmp)
        tmp = 0
        for i in range(len(s))[::-1]:
            if s[i] not in s[i + 1:]:
                tmp += 1
            r_count.append(tmp)
        r_count = r_count[::-1]
        count = 0
        for i in range(len(r_count) - 1):
            if l_count[i] == r_count[i + 1]:
                count += 1
        return count
