from bisect import bisect
from collections import defaultdict

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        ans = -1
        count = defaultdict(int)
        tmp = []
        
        for i, a in enumerate(arr):
            index = bisect(tmp, a)
            add = 0

            if index != 0 and tmp[index-1] + 1 == a:
                count[tmp[index-1] - tmp[index-2] + 1] -= 1
                k = tmp.pop(index-1)
                tmp.insert(index-1, a)
                count[a - tmp[index-2] + 1] += 1
                add += 1
                # print('<', tmp, count)
            if index < len(tmp) - 1 and tmp[index] -1 == a:
                count[tmp[index+1] - tmp[index] + 1] -= 1
                k = tmp.pop(index)
                tmp.insert(index, a)
                count[tmp[index+1] - a + 1] += 1
                add += 1
                # print('>', tmp, count)
                
            if add == 0:
                tmp.insert(index, a)
                tmp.insert(index, a)
                count[1] += 1
            elif add == 2:
                count[a - tmp[index-2] + 1] -= 1
                count[tmp[index+1] - a + 1] -= 1
                count[tmp[index+1] - tmp[index-2] + 1] += 1
                tmp.pop(index)
                tmp.pop(index-1)
            
            # print(tmp, count)
            if count[m] > 0:
                ans = i + 1
        
        # print('-' * 20)
        # s = ['0' for _ in range(len(arr))]
        # def exist(s, m):
        #     p = ''.join(s).split('0')
        #     return any(len(x) == m for x in p)
        # for i, a in enumerate(arr):
        #     s[a-1] = '1'
        #     if exist(s, m):
        #         ans = i + 1
        return ans
