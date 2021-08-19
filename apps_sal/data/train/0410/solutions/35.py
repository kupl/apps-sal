class Solution:

    def __init__(self):
        self.cache = {1: 0, 2: 1, 3: 7, 4: 2}

    def getPower(self, n):
        after = 0
        steps = 0
        if n % 4 == 0:
            after = n // 4
            steps = 2
        elif n % 4 == 1:
            after = n // 4 * 3 + 1
            steps = 3
        elif n % 4 == 2:
            after = n // 4 * 3 + 2
            steps = 3
        else:
            after = n // 4 * 9 + 8
            steps = 4
        if after in list(self.cache.keys()):
            return self.cache[after] + steps
        else:
            return self.getPower(after) + steps

    def getKth(self, low, high, k):
        data = [self.getPower(i) for i in range(low, high + 1)]
        sorted_data = sorted(zip(data, list(range(len(data)))), key=lambda x: x[0])
        return sorted_data[k - 1][1] + low
