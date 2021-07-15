class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a or b or c:
            temp = (a & 1) | (b & 1)
            if temp != (c & 1):
                if c & 1:
                    count += 1
                else:
                    if a & 1:
                        count += 1
                    if b & 1:
                        count += 1
            a = a >> 1
            b = b >> 1
            c = c >> 1
        return count
