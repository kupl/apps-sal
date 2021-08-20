class Solution:

    def queryString(self, S: str, N: int) -> bool:
        seen = set()
        if len(S) < 2:
            seen.add(S)
        for i in range(len(S) - 1):
            for j in range(i + 1, len(S)):
                if S[i] == '0':
                    seen.add(S[i + 1:j + 1])
                else:
                    seen.add(S[i:j + 1])
        for i in range(1, N + 1):
            binary = bin(i)[2:]
            if binary not in seen:
                return False
        return True
