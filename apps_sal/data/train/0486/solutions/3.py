class Solution:

    def queryString(self, S: str, N: int) -> bool:
        for i in range(1, N + 1):
            curr = bin(i)[2:]
            if S.find(curr) == -1:
                return False
        return True
