class Solution:
    def minOperationsMaxProfit(self, arr: List[int], boardingCost : int, runningCost : int) -> int:
        # Dividing people in the groups of <=4
        grps = []
        # length of customers array
        n = len(arr)
        # rem--> number of people waiting
        rem = 0
        
        # traversing the customers array
        for i in range(n):
            # total number of people available right now 
            avail = arr[i]+rem
            # number of available people >=4 then append grp of 4 and update remaining [rem]
            if avail>=4:
                avail-=4
                grps.append(4)
                rem = avail
            # number of available people <4  then make group of available people and update remaining [rem=0]
            else:
                rem = 0
                grps.append(avail)
        
        # make groups of 4 until remaining >=4 otherwise make <4 and break
        while rem>0:
            if rem>=4:
                rem-=4
                grps.append(4)
            else:
                grps.append(rem)
                rem = 0
        
        # mex--> represents maximum profit
        mex = -10**10
        # cost--> represents current total cost
        cost = 0
        # ind --> represents rotation number
        ind = 0
        for i in range(len(grps)):
            # calculate net cost till now
            cost+= boardingCost*grps[i]-runningCost
            # upadte max profit and rotation number
            if mex<cost:
                mex = max(mex,cost)
                ind = i+1
        # max profit< 0
        if mex<0:
            return -1
        # return rotation number
        return ind
