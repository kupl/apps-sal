class Solution:

    def transform(self, num, count=0):
        if num == 1:
            return count
        elif num % 2 == 0:
            return self.transform(num // 2, count + 1)
        else:
            return self.transform(num * 3 + 1, count + 1)

    def getKth(self, lo: int, hi: int, k: int) -> int:
        p_list = []
        for i in range(lo, hi + 1):
            p_list.append((self.transform(i), i))
        p_list.sort()
        return p_list[k - 1][1]
