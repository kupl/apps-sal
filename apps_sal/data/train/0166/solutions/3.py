class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a = bin(a)[2:].zfill(32)
        b = bin(b)[2:].zfill(32)
        c = bin(c)[2:].zfill(32)
        count = 0

        for i in range(32):
            temp_a = int(a[i])
            temp_b = int(b[i])
            temp_c = int(c[i])

            if temp_a | temp_b != temp_c:
                if temp_c == 1:
                    count += 1
                else:
                    if temp_a == 1:
                        count += 1
                    if temp_b == 1:
                        count += 1
        return count
