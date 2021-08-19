class Solution:

    def knightDialer(self, n: int) -> int:
        dic = {0: (4, 6), 1: (6, 8), 2: (7, 9), 3: (4, 8), 4: (0, 3, 9), 5: (), 6: (1, 0, 7), 7: (2, 6), 8: (1, 3), 9: (2, 4)}
        prev_dic = {}
        for i in range(10):
            prev_dic[i] = 1
        for i in range(n - 1):
            cur_dic = collections.defaultdict(int)
            for j in prev_dic:
                for k in dic[j]:
                    cur_dic[k] += prev_dic[j]
            prev_dic = cur_dic
        return sum(prev_dic.values()) % (10 ** 9 + 7)
