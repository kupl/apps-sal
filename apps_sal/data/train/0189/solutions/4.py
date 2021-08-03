class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        unhappy = [0] * n
        for i in range(n // 2):
            a, b = pairs[i]
            b_a_idx, a_b_idx = preferences[b].index(a), preferences[a].index(b)
            for j in range(i + 1, n // 2):
                c, d = pairs[j]
                c_a_idx = preferences[c].index(a)
                c_b_idx = preferences[c].index(b)
                c_d_idx = preferences[c].index(d)

                d_a_idx = preferences[d].index(a)
                d_b_idx = preferences[d].index(b)
                d_c_idx = preferences[d].index(c)

                a_c_idx = preferences[a].index(c)
                a_d_idx = preferences[a].index(d)

                b_c_idx = preferences[b].index(c)
                b_d_idx = preferences[b].index(d)

                # a <-> c
                if c_a_idx < c_d_idx and a_c_idx < a_b_idx:
                    unhappy[a] = unhappy[c] = 1
                # a <-> d
                if d_a_idx < d_c_idx and a_d_idx < a_b_idx:
                    unhappy[a] = unhappy[d] = 1
                # b <-> c
                if c_b_idx < c_d_idx and b_c_idx < b_a_idx:
                    unhappy[b] = unhappy[c] = 1
                # b <-> d
                if d_b_idx < d_c_idx and b_d_idx < b_a_idx:
                    unhappy[b] = unhappy[d] = 1
        return sum(unhappy)
