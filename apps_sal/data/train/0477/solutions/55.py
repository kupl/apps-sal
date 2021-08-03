class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        if n == 2:
            return ['0', '1', '1'][k - 1]
        record = [0, 1, 1]
        for i in range(n - 2):
            record = record + [1] + record
            l = len(record)
            record[l // 2 + l // 2 // 2 + 1] = 0

        return str(record[k - 1])
