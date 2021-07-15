class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # 8:49 9/26/20
        
        def find_difficulty(d, w):
            n = len(d)
            lt, rt = 0, n
            while lt < rt:
                mid = lt + (rt - lt) // 2
                if d[mid] == w:
                    return mid
                elif d[mid] > w:
                    rt = mid
                else:
                    lt = mid + 1
            return rt-1

        difficulty1 = sorted(difficulty)
        
        difficulty = list(zip(difficulty, profit))
        difficulty.sort(key = lambda x: (x[0]))
        
        profit = {}
        max_profit = 0
        for i in range(len(difficulty)):
            if difficulty[i][0] not in profit or profit[difficulty[i][0]] < difficulty[i][1]:
                profit[difficulty[i][0]] = difficulty[i][1]
            max_profit = max(max_profit, profit[difficulty[i][0]])
            profit[difficulty[i][0]] = max_profit
                
        
        total = 0
        pre = -1
        for i in range(len(worker)):
            # if i > 0 and worker[i] == worker[i-1] and pre != -1:
            #     total += profit[pre]
            #     continue
            pre = find_difficulty(difficulty1, worker[i])
            if pre != -1:
                total += profit[difficulty1[pre]]
                
        return total
            
        

