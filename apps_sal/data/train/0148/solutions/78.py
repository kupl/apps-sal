class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
            difficulty_price = sorted(list(zip(difficulty, profit)), key = lambda x: (x[0], x[1]))    
            max_prices = []
            n = -1
            curr_price = 0
            for i in range(max(difficulty)+1):
                if i == difficulty_price[n+1][0]:
                    n+=1
                    while n < len(difficulty_price) - 1 and i == difficulty_price[n+1][0]:
                        n+=1
                    if difficulty_price[n][1] > curr_price:
                        curr_price = difficulty_price[n][1]
                max_prices.append(curr_price)
            profit_sum = 0
            for sub_worker in worker:
                if sub_worker >= len(max_prices):
                    profit_sum += max_prices[-1]
                else:
                    profit_sum += max_prices[sub_worker]
            return profit_sum
