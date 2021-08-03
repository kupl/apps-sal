from collections import defaultdict


class Solution:
    def minDays(self, n):
        dic = {n: 0}
        while 0 not in dic:
            temp = defaultdict(int)
            for i, v in list(dic.items()):
                if i % 2 == 0:
                    temp[i // 2] = v + 1
                if i % 3 == 0:
                    temp[i // 3] = v + 1
                temp[i - 1] = v + 1
            dic = temp.copy()
        return dic[0]
