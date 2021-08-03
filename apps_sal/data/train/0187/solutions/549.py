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
            if (customer * boardingCost - runningCost) + profit1[0] > profit1[0]:
                profit2[0] = (customer * boardingCost - runningCost) + profit1[0]
                profit2[1] = profit1[1] + 1

            profit1[0] = (customer * boardingCost - runningCost) + profit1[0]
            profit1[1] = profit1[1] + 1
            cur += 1

        if left:
            profit1[0] += (left // 4) * (customer * boardingCost - runningCost)
            profit1[1] += (left // 4)

            if (left % 4) * boardingCost - runningCost > 0:
                profit1[0] += (left % 4) * boardingCost - runningCost
                profit1[1] += 1

        if profit1[0] > profit2[0]:
            return profit1[1]
        elif profit1[0] < profit2[0]:
            return profit2[1]
        else:
            return min(profit1[1], profit2[1])

        '''
        while cur<len(customers):
            current = customers[cur]

            if current >=4:
                
                profit1[cur+1][0]= (current//4)*(4*boardingCost-runningCost)+profit1[cur][0]
                profit1[cur+1][1] = profit1[cur][1] +current//4
                current = current%4               
                if profit1[cur][0]<profit1[cur+1][0]:
                    profit2[cur+1][0]=profit1[cur+1][0]
                    profit2[cur+1][1]=profit1[cur+1][1]
                else:
                    profit2[cur+1][1]=profit1[cur][1]
                    profit2[cur+1][0]=profit1[cur][0]
                    
                if current>0:
                    profit1[cur+1][0]=current*boardingCost-runningCost+profit1[cur+1][0]
                    profit1[cur+1][1]=profit1[cur+1][1]+1 
            
            else:

                profit1[cur+1][0]=current*boardingCost-runningCost+profit1[cur][0]

                profit1[cur+1][1]=profit1[cur][1]+1 

                
                
                
                profit2[cur+1][1]=profit1[cur][1]

                profit2[cur+1][0]=profit1[cur][0]

            
            
                    

            cur+=1
            

        
        keys1 = list(range(len(customers)+1))
        keys2= list(range(len(customers)+1))
        keys1.sort(key=lambda x: (profit1[x][0],-profit1[x][1]))
        keys2.sort(key=lambda x:(profit2[x][0],-profit2[x][1]))

        key1= keys1[-1]
        key2 = keys2[-1]
        print(profit1)
        print(profit2)

        if profit1[key1][0]>profit2[key2][0]:
            return profit1[key1][1]
        elif profit1[key1][0]<profit2[key2][0]:
            return profit2[key1][1]
        else:
            return min(profit1[key1][1],profit2[key2][1])
        '''
