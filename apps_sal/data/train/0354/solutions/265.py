class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        if n == 1:
            return 6
        states = []
        for i in rollMax:
            states.append([0] * i)
            states[-1][0] = 1
        sums = [0] * 6
        for i in range(1, n):
            for i in range(6):
                sums[i] = sum(states[i])
            for i in range(6):
                for j in reversed(list(range(len(states[i])))):
                    if j == 0:
                        states[i][0] = sum([sums[index] for index in range(6) if index != i]) % (10 ** 9 + 7)
                    else:
                        states[i][j] = states[i][j - 1]
        return sum([sum(x) for x in states]) % (10 ** 9 + 7)
