class Solution:

    def queryString(self, S: str, N: int) -> bool:
        for i in range(1, N + 1):
            b = bin(i).replace('0b', '')
            if b not in S:
                return False
        return True
