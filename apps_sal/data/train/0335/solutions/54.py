from collections import defaultdict

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        memo = defaultdict(int)
        memo[0] = 0
        
        for rod in rods:
            temp_memo = defaultdict(int)
            keys = list(memo.keys())
            for k in keys:
                temp_memo[k + rod] = max(memo[k] + rod, temp_memo[k + rod])
                temp_memo[k - rod] = max(memo[k], temp_memo[k - rod])
                temp_memo[k] = max(memo[k], temp_memo[k])
            memo.update(temp_memo)
        return memo[0]
                
        

