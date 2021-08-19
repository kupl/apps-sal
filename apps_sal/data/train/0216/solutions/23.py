chars = ['c', 'r', 'o', 'a', 'k']
C = len(chars)
cs = set(chars)


class Solution:

    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        N = len(croakOfFrogs)
        if N == 0:
            return 0
        if N % 5 != 0:
            return -1
        counter = Counter(croakOfFrogs)
        if len(counter) != 5:
            return -1
        totFreq = None
        for c in counter:
            if not totFreq:
                totFreq == counter[c]
            elif totFreq != counter[c]:
                return -1
        dic = [0] * C
        ans = 0
        for i in range(N):
            c = croakOfFrogs[i]
            if c not in cs:
                return -1
            if c == chars[0]:
                for j in range(1, len(chars)):
                    dic[j] += 1
                ans = max(ans, dic[C - 1])
            else:
                j = chars.index(c)
                dic[j] -= 1
                prev = dic[j]
                for k in range(j - 1, -1, -1):
                    if dic[k] > prev:
                        return -1
                    prev = dic[k]
        return ans
