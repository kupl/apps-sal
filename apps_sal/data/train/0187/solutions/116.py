class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        b = 0
        w = 0
        r = 0
        tc = 0
        '\n        for i in customers:\n            w+=i\n            tc+=i\n            #bd = min(4,w)\n            #w-=bd\n            if w//4 == 0:\n                r+=1\n            else:\n                r+= (w//4)    \n            print(r)\n            \n            if w<4:\n                w-=w\n            else:\n                w-= (4*(w//4))\n            print("     ",w)\n        '
        i = 0
        n = len(customers)
        while True:
            if i == n:
                x = w // 4
                r += x
                if w % 4 != 0 and w % 4 * boardingCost > runningCost:
                    r += 1
                break
            w += customers[i]
            tc += customers[i]
            bd = min(4, w)
            w -= bd
            r += 1
            i += 1
        return r if tc * boardingCost - runningCost * r > 0 else -1
