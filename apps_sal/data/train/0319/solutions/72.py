class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @lru_cache(None)
        def helper(idx):
            if idx == len(stoneValue): return 0, idx
            # if idx + 2 >= len(stoneValue) - 1: return sum(stoneValue[idx:]), len(stoneValue)
            score, max_score = 0, -sys.maxsize + 1
            op_idx = idx + 1
            for num in range(3):
                if idx + num < len(stoneValue):
                    score += stoneValue[idx + num]
                    b_score, a_idx = helper(idx + num + 1)
                    if helper(a_idx)[0] + score >= max_score:
                        max_score = helper(a_idx)[0] + score
                        op_idx = idx + num + 1
            return max_score, op_idx
        
        score, op_idx = helper(0)
        op_score = helper(op_idx)[0]
        
        # print(score, op_idx)
        if score > op_score: return 'Alice'
        elif score == op_score: return 'Tie'
        else: return 'Bob'
            

