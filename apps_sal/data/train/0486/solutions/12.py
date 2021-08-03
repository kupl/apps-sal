from itertools import combinations


class Solution:
    def queryString(self, S: str, N: int) -> bool:
        d = set()
        for i in range(0, len(S) + 1):
            j = 0
            end = i + 1
            while end < len(S) + 1:
                d.add(S[j:end])
                j = j + 1
                end = end + 1
        q = 1
        for i in range(1, N + 1):
            if bin(i)[2:] not in d:
                q = 0
                break
        # print(type(bin(3)[2:]))
        return q
