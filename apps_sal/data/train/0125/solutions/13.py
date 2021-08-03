class Solution:
    def superPow(self, a, b):
        result = 1
        x = a % 1337
        for y in b[::-1]:
            result = (result * (x**y)) % 1337
            x = (x**10) % 1337
        return result
