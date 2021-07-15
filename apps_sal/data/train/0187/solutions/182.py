class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
        result = []
        maxval = 0
        Current_profit = 0
        
        board_list = 0
        total_board = 0
        count = 0
        i = 1
        j = 1
        
        for x in range(0,len(customers)):
            #print(x)
            if customers[x] != 0:
                wait_list = customers[x]
                i += x
                break
            else:
                count += 1
        #print(\"Waiting List & x\",wait_list,i)
        while wait_list != 0:
            
            if wait_list >= 4:
                total_board +=  4
                wait_list -= 4
            else:
                total_board += wait_list
                wait_list -= wait_list
            #print(total_board,j)
            Current_profit = total_board * boardingCost - j * runningCost
            if i < len(customers):
                wait_list += customers[i]
                i += 1
            j += 1
            result.append(Current_profit)
            #print(Current_profit)
        #print(result)
        #print(result[992])
        #print(len(result))
        maxval = max(result)
        #print(maxval)
        
        if maxval < 0:
            return -1
        else:
            return result.index(maxval) + 1 + count
        #return Current_profit
            

