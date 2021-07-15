class Solution:
    def minInteger(self, num: str, k: int) -> str:
        D = 10
        ans = num
        for d in range(D):
            i = num.find(str(d))
            if i < 0:
                continue
            cost = i
            if cost > k:
                continue
            if i == 0:
                return num[i] + self.minInteger(num[i + 1:], k)
            return num[i] + self.minInteger(num[:i] + num[i + 1:], k - cost)
        return num
