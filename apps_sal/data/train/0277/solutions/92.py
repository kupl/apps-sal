class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        max_idx = float('-inf')
        cnt = 0
        for i in range(len(light)):
            max_idx = max(max_idx, light[i])
            if max_idx == i + 1:
                cnt += 1
        return cnt
