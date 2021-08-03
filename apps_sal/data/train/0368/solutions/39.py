class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        if satisfaction[-1] <= 0:
            return 0
        last_sum = 0
        temp = [0] * len(satisfaction)
        for i in range(len(satisfaction), 0, -1):
            temp = [a + b for a, b in zip(temp, [0] * (i - 1) + satisfaction[i - 1:])]
            score = sum(temp)
            if last_sum > score:
                break
            last_sum = score

        return last_sum
