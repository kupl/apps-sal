class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        length, res = len(satisfaction), 0
        l = [0] * length

        for i in range(length):
            summ = 0
            for j in range(i + 1):
                l[j] += satisfaction[j]
                summ += l[j]

            if summ > res:
                res = summ

        return res
