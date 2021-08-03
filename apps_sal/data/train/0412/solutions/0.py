from math import comb
from math import pow


class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if(target < d * 1 or target > d * f):
            return 0
        target = target - d
        sum = 0
        i = 0
        j = 0
        while(i <= target):
            y = target - i
            if(j % 2 == 0):

                sum = int((sum + comb(d, j) * comb(y + d - 1, y)))
            else:
                sum = int((sum - comb(d, j) * comb(y + d - 1, y)))
            #print( comb(d, j) * comb(y+d-1,y))
            #print('i ={} y= {} sum={}  '.format(i,y,sum))
            j = j + 1
            i = i + f

        # print(sum)
        return int(sum) % 1000000007
