class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        mat = [[[0,0] for c in range(n)] for r in range(n)]
        for r in range(n):
            mat[r][r][0] = piles[r]
        for diff in range(1,n):
            for r in range(0, n-diff):
                c = r + diff
                left_ = mat[r][c-1]
                picker_1 = left_[1]+piles[c]
                other_1 = left_[0]
                right_ = mat[r+1][c]
                picker_2 = right_[1] + piles[r]
                other_2 = right_[0]
                mat[r][c] = (max(picker_1, picker_2), min(other_1, other_2))
                
        if mat[-1][-1][0] > mat[-1][-1][1]:
            return True
        return False

