class Solution:
    def queryString(self, S: str, N: int) -> bool:

        dic = set()

        for i in range(len(S)):
            for l in range(len(S) - i):
                dic.add(S[i:i + l + 1])
        for x in range(1, N + 1):
            if str(bin(x)[2:]) not in dic:
                return False
        return True
