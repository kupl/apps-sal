# cook your dish here
def max_profit(prices,n,k):

 profit = [[0 for i in range(n)] for j in range(k+1)] 
 for i in range(1,k+1):

  diff = (-1)*prices[0]
  for j in range(1,n):
   diff = max(profit[i-1][j]-prices[j],diff)
   profit[i][j] = max(profit[i][j-1],diff+prices[j])
 
 return profit[k][n-1]
 
try:
 n,k = map(int,input().split())
 prices = [int(input()) for _ in range(n)]
 print(max_profit(prices,n,k//2))

except:
 pass
