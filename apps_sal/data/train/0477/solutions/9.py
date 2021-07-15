class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # First element is for n == 1
        cache = [''] * n

        def gen_str(n):
            if n-1 in cache:
                return cache[n-1]

            if n == 1:
                s = '0'
                cache[0] = s
                return s

            prev = gen_str(n-1)
            s = prev + '1'
            for c in reversed(prev):
                if c == '0':
                    s += '1'
                else:
                    s += '0'
            cache[n-1] = s
            return s

        return gen_str(n)[k-1]
