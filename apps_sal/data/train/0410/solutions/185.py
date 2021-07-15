import heapq
from operator import itemgetter

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {1: 0, 2: 1}
        num_to_power = []
        
        for num in range(lo, hi + 1):

            if num == 1:
                num_to_power.append((num, 0))
                continue
                
            i = num
            steps = 0   
            while i != 1:
                if i in memo:
                    num_to_power.append((num, steps + memo[i]))
                    memo[num] = steps + memo[i]
                    i = 1
                elif  i % 2 == 0:
                    i = i // 2
                    steps += 1
                else:
                    i = 3 * i + 1
                    steps += 1

        num_to_power = sorted(num_to_power, key=itemgetter(1,0))
        return num_to_power[k - 1][0]
