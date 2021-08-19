class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        acc = []
        temp = 0
        ones = 0
        for u in arr:
            temp += u % 2
            temp %= 2
            if temp == 1:
                ones += 1
        L = len(arr)
        return ones * (L - ones + 1) % (10 ** 9 + 7)
