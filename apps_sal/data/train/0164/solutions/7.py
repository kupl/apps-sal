class Solution:

    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        if k <= 0:
            return num
        if k >= (n + 1) * n // 2:
            return ''.join(sorted(num))
        for i in range(10):
            index = num.find(str(i))
            if 0 <= index <= k:
                return str(num[index]) + self.minInteger(num[:index] + num[index + 1:], k - index)
        return num
