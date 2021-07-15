class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        for i in range(2**k):
            bin_value = bin(i)[2:] if len(bin(i)[2:]) == k else '0' * (k - len(bin(i)[2:])) + bin(i)[2]
            if bin_value not in s:
                return False
        return True
            

