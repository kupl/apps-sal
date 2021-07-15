class Solution:
    def minOperationsMaxProfit(self, arr, bc, rc):
        # ok
        profit = 0
        turn = 0
        maxProfit = 0
        pref = []
        tillnow = 0
        till=0
        ansturn=0

        s = 0
        for i in arr:s+=i;pref.append(s)

        n = len(arr)
        for i in range(n):
            now = pref[i]-till
            if now>=4:
                till+=4
                now-=4
                profit+=(4*bc - rc)
            else:
                till+=now
                profit+=(now*bc - rc)
                now=0
            turn+=1
            if profit>maxProfit:
                ansturn=turn
                maxProfit=profit
        while now>0:
            if now>=4:
                now-=4
                profit+=(4*bc-rc)
                turn+=1
            else:
                profit+=(now*bc-rc)
                now=0
                turn+=1
            if profit>maxProfit:
                ansturn=turn
                maxProfit=profit
        if maxProfit==0:
            return -1
        else:
            return ansturn
