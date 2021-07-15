from collections import defaultdict
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix = defaultdict(list)
        best_till = [sys.maxsize] * len(arr)
        res = sys.maxsize
        prefix[0].append(-1)
        temp_s = 0
        for i, ele in enumerate(arr):
            temp_s += ele
            prefix[temp_s].append(i)
            #print(i, temp_s)
            if temp_s - target in prefix:
                for index in prefix[temp_s - target]:
                    best_till[i] = min(best_till[i - 1], i - index)
                    if index != -1:
                        res = min(res, best_till[index] + i - index) 
                    #print(\"found\", i, index, temp_s, best_till[i], res)
            else:
                if i >= 1:
                    best_till[i] = best_till[i - 1]
        #print(\"best_till\", best_till)
        return -1 if res == sys.maxsize else res
        

