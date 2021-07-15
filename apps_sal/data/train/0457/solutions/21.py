class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        numpath = [0] + [float('inf')] * (amount) # 가장 큰 값으로 amount + 1만큼 배열을 초기화
        
        for coin in coins:
            for i in range(coin, amount + 1):
                # 처음 도착한 위치: numpath[i] = inf, numpath[i - coin] + 1 = inf
                # 처음 도착한 곳이 아닌 위치: numpath[i] = 이전까지 이 위치에 올 수 있었던 최소 동전 개수
                # numpath[i - coin] + 1 = 이번 coin만큼 건너띄기 전의 값에 + 1을 해준 최소 동전 개수 
                if numpath[i] > 1 + numpath[i - coin]:
                    numpath[i] = 1 + numpath[i - coin]
                
        return numpath[amount] if numpath[amount] != float('inf') else -1 # amount가 inf가 아닌 경우에 최소 동전 개수가 nunpath[amount]에 저장
