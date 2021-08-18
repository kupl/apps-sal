class Solution:
    def minDays(self, n: int) -> int:
        result = 0
        q = [n]
        while q:
            next = set()
            for remain in q:
                if remain == 1:
                    return result + 1
                if remain % 2 == 0:
                    next.add(remain // 2)
                if remain % 3 == 0:
                    next.add(remain // 3)
                next.add(remain - 1)
            result += 1
            q = next
        return result
