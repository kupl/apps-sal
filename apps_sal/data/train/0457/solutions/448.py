class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = Counter(coins)

        def recurse(left, count) -> int:
            if left in m:
                return m[left]
            
            if left == 0:
                m[left] = count
                return count
            
            smallest = math.inf
            for c in coins:
                if left - c >= 0:
                    smallest = min(smallest, recurse(left-c, count+1))
                
            m[left] = smallest+1
            return smallest+1

        recurse(amount,0)

        if m[amount] == math.inf:
            return -1
        return m[amount]
