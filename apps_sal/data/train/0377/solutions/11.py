class Solution:

    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        a_t = A
        b_t = B
        col = []
        low_anc = a_t
        while a_t != b_t:
            if a_t < b_t:
                col.append(a_t)
                a_t = a_t + A
            else:
                col.append(b_t)
                b_t = b_t + B
        col.append(a_t)
        low_anc = a_t
        idx = (N - 1) % len(col)
        ans = (N - 1) // len(col) * low_anc + col[idx]
        return ans % (10 ** 9 + 7)
