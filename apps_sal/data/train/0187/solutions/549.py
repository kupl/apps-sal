class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        cur = 0
        total = 0
        profit1 = [0, 0]
        profit2 = [0, 0]
        stop = False
        left = 0
        if 4 * boardingCost - runningCost <= 0:
            return -1
        while cur < len(customers):
            left += customers[cur]
            if left >= 4:
                left -= 4
                customer = 4
            else:
                customer = left
                left = 0
            if customer * boardingCost - runningCost + profit1[0] > profit1[0]:
                profit2[0] = customer * boardingCost - runningCost + profit1[0]
                profit2[1] = profit1[1] + 1
            profit1[0] = customer * boardingCost - runningCost + profit1[0]
            profit1[1] = profit1[1] + 1
            cur += 1
        if left:
            profit1[0] += left // 4 * (customer * boardingCost - runningCost)
            profit1[1] += left // 4
            if left % 4 * boardingCost - runningCost > 0:
                profit1[0] += left % 4 * boardingCost - runningCost
                profit1[1] += 1
        if profit1[0] > profit2[0]:
            return profit1[1]
        elif profit1[0] < profit2[0]:
            return profit2[1]
        else:
            return min(profit1[1], profit2[1])
        '\n        while cur<len(customers):\n            current = customers[cur]\n\n            if current >=4:\n                \n                profit1[cur+1][0]= (current//4)*(4*boardingCost-runningCost)+profit1[cur][0]\n                profit1[cur+1][1] = profit1[cur][1] +current//4\n                current = current%4               \n                if profit1[cur][0]<profit1[cur+1][0]:\n                    profit2[cur+1][0]=profit1[cur+1][0]\n                    profit2[cur+1][1]=profit1[cur+1][1]\n                else:\n                    profit2[cur+1][1]=profit1[cur][1]\n                    profit2[cur+1][0]=profit1[cur][0]\n                    \n                if current>0:\n                    profit1[cur+1][0]=current*boardingCost-runningCost+profit1[cur+1][0]\n                    profit1[cur+1][1]=profit1[cur+1][1]+1 \n            \n            else:\n\n                profit1[cur+1][0]=current*boardingCost-runningCost+profit1[cur][0]\n\n                profit1[cur+1][1]=profit1[cur][1]+1 \n\n                \n                \n                \n                profit2[cur+1][1]=profit1[cur][1]\n\n                profit2[cur+1][0]=profit1[cur][0]\n\n            \n            \n                    \n\n            cur+=1\n            \n\n        \n        keys1 = list(range(len(customers)+1))\n        keys2= list(range(len(customers)+1))\n        keys1.sort(key=lambda x: (profit1[x][0],-profit1[x][1]))\n        keys2.sort(key=lambda x:(profit2[x][0],-profit2[x][1]))\n\n        key1= keys1[-1]\n        key2 = keys2[-1]\n        print(profit1)\n        print(profit2)\n\n        if profit1[key1][0]>profit2[key2][0]:\n            return profit1[key1][1]\n        elif profit1[key1][0]<profit2[key2][0]:\n            return profit2[key1][1]\n        else:\n            return min(profit1[key1][1],profit2[key2][1])\n        '
