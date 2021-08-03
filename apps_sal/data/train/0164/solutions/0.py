class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        if k <= 0:
            return num

        if k > n * (n - 1) // 2:
            return ''.join(sorted(list(num)))

        for i in range(10):
            idx = num.find(str(i))
            if idx >= 0 and idx <= k:
                return num[idx] + self.minInteger(num[:idx] + num[idx + 1:], k - idx)
