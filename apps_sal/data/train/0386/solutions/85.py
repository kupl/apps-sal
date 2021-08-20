class Solution:

    def countVowelPermutation(self, n):
        (last_a, last_e, last_i, last_o, last_u) = (1, 1, 1, 1, 1)
        mod = round(1000000000.0 + 7)
        for i in range(n - 1):
            cur_a = (last_e + last_i + last_u) % mod
            cur_e = (last_a + last_i) % mod
            cur_i = (last_e + last_o) % mod
            cur_o = last_i % mod
            cur_u = (last_i + last_o) % mod
            (last_a, last_e, last_i, last_o, last_u) = (cur_a, cur_e, cur_i, cur_o, cur_u)
        return sum([last_a, last_e, last_i, last_o, last_u]) % mod
