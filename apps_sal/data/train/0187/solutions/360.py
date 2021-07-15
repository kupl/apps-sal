class Solution:
    def minOperationsMaxProfit(self, customers: List[int], bc: int, rc: int) -> int:
        rnd = waiting = 0
        ans = -1
        profit = -1
        curp = 0
        
        n = sum(customers)
        debug = 0
        if debug:
            print(f'lenght is {len(customers)}, total cust is {n} where n % 4 = {n%4}, boardingTicket is {bc}, run cost is {rc}')
        
        i = 0
        while i < len(customers) or waiting > 0:
            cust = 0 if i >= len(customers) else customers[i]
            waiting += cust
            board = min(4, waiting)
            waiting -= board
            curp = curp + board * bc - rc
            rnd += 1
            if i < len(customers):
                i += 1
            if debug:
                print(f'i is {i}, new comer is {cust} and total waiting is {waiting}, '
                      f'board {board} people, curp is {curp}, rnd = {rnd}')            
        #for i, cust in enumerate(customers):
            # if waiting <= 4:
            #     curp = curp + waiting * bc - rc
            #     if debug:
            #         print(f'i is {i}, new comer is {cust} and total waiting is {waiting}, '
            #               f'board {waiting} people, curp is {curp}, rnd = {rnd + 1}')
            #     waiting = 0
            #     rnd += 1
            # else:
            #     board = waiting - waiting % 4
            #     boardrnd = board // 4
            #     curp = curp + board * bc - boardrnd * rc  # t * (4*bc - rc)
            #     if debug:
            #         print(f'i is {i}, new comer is {cust} and total waiting is {waiting}, '
            #               f'board {board} people, curp is {curp}, rnd = {rnd + boardrnd}')
            #     waiting %= 4
            #     rnd += boardrnd
            
            if curp > profit:
                profit = curp
                ans = rnd
                
        if waiting > 0:
            curp = curp + waiting * bc - rc
            rnd += 1
            if debug:
                print(f'i is n, new comer is 0 and total waiting is {waiting}, board {waiting} people, curp is {curp}, rnd = {rnd}')
            if curp > profit:
                profit = curp
                ans = rnd
        return ans
    
    

# [17,0,45,39,19,4,9,3,16]
# 11
# 33

