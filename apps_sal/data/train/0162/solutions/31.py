class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) < len(text1):
            text1, text2 = text2, text1

        previous = [0] * (len(text1) + 1)

        for col in reversed(range(len(text2))):
            current = [0] * (len(text1) + 1)
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    current[row] = 1 + previous[row + 1]
                else:
                    current[row] = max(previous[row], current[row + 1])
            previous = current

        return previous[0]

        '''
        dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
                else:
                    dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])
        
        return dp_grid[0][0]
        '''

        '''
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):
            
            if p1 == len(text1) or p2 == len(text2):
                return 0
            
            if text1[p1] == text2[p2]:
                return 1 + memo_solve(p1 + 1, p2 + 1)
            
            else:
                return max(memo_solve(p1, p2 + 1), memo_solve(p1 + 1, p2))
            
        return memo_solve(0, 0)
        '''

        '''
        def memo_solve(p1, p2):
            
            if p1 == len(text1) or p2 == len(text2):
                return 0
            
            option_1 = memo_solve(p1 + 1, p2)
            
            first_occurence = text2.find(text1[p1], p2)
            option_2 = 0
            if first_occurence != -1:
                option_2 = 1 + memo_solve(p1 + 1, first_occurence + 1)
            
            return max(option_1, option_2)
                
        return memo_solve(0, 0)'''
