class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        current_char = 'A'
        current_max = 0
        answer = 0
        for (i, c) in enumerate(cost):
            if s[i] == current_char:
                if current_max < c:
                    answer += current_max
                    current_max = c
                else:
                    answer += c
            else:
                current_char = s[i]
                current_max = c
        return answer
