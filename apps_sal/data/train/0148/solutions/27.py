class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        
        data = sorted([(d,p) for d,p in zip(difficulty, profit)])
        worker.sort()
        i, n, money = 0, len(data), 0
        res = 0
        for w in worker:
            while i < n and w >= data[i][0]:
                money = max(money, data[i][1])
                i += 1
            res += money
        return res
        
        
        

