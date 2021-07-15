class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        print(bin(a))
        print(bin(b))
        print(bin(c))
        while a or b or c:
            # print(a, b, c)
            if c % 2:
                if not (a % 2 or b % 2):
                    flips += 1
            else:
                flips += a % 2 + b % 2
            a //= 2
            b //= 2
            c //= 2
        return flips
