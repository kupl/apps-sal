class Solution:
    def knightDialer(self, n: int) -> int:
        cur_state = [1 for _ in range(10)]
        mod = 10 ** 9 + 7
        edges = [(1, 6), (1, 8), (2, 7), (2, 9), (3, 4), (3, 8), (4, 9), (4, 0), (6, 7), (6, 0)]
        edge_dic = { i: [] for i in range(10) }
        for i, j in edges:
            edge_dic[i].append(j)
            edge_dic[j].append(i)

        for _ in range(1, n):
            new_state = [0 for _ in range(10)]
            for i in range(10):
                new_state[i] = sum([cur_state[j] for j in edge_dic[i]]) % mod
            cur_state = new_state
        
        return sum(cur_state) % mod

