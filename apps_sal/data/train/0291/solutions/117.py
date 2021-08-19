class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] ^ num & 1)
        zeros = 0
        ones = 0
        result = 0
        for x in prefix:
            if x == 1:
                ones += 1
                result += zeros
            else:
                zeros += 1
                result += ones
        return result % (10 ** 9 + 7)
