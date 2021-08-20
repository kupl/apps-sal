class Solution:

    def queryString(self, S: str, N: int) -> bool:

        def is_x_in(x):
            binary = []
            while x:
                binary.append(x % 2)
                x = x >> 1
            binary = ''.join((str(n) for n in reversed(binary)))
            return S.find(binary) >= 0
        return all((is_x_in(x) for x in range(N + 1)))
