class Solution:

    def superPow(self, a, b):
        result = 1
        fermatb = int(''.join(map(str, b))) % 570
        while fermatb:
            if fermatb & 1:
                result = result * a % 1337
            a = a * a % 1337
            fermatb >>= 1
        return result
