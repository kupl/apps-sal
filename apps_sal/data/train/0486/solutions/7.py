class Solution:

    def queryString(self, S: str, N: int) -> bool:
        substrings = set()
        for i in range(len(S)):
            for j in range(i, len(S) + 1):
                substrings.add(S[i:j])
        for i in range(1, N + 1):
            binN = str(bin(i))[2:]
            if binN in substrings:
                continue
            else:
                return False
        return True
