class Solution:
    def minInteger(self, num: str, k: int) -> str:
        if k <= 0:
            return num
        for i in range(10):
            ind = num.find(str(i))
            if 0 <= ind <= k:
                return str(num[ind]) + self.minInteger(num[0:ind] + num[ind + 1:], k - ind)
        return num
