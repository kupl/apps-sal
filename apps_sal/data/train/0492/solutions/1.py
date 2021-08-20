class Solution:

    def strWithout3a3b(self, A: int, B: int) -> str:
        count = [A, B]
        char = ['aab', 'bba']
        for i in range(2):
            j = i ^ 1
            if count[i] >= count[j]:
                if count[i] >= count[j] * 2:
                    return char[i] * count[j] + char[i][:1] * (count[i] - count[j] * 2)
                return char[i] * (count[i] - count[j]) + char[i][1:] * (count[j] * 2 - count[i])
