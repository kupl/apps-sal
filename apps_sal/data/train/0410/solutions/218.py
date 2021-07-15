class Solution:
    def __init__(self):
        self.cache = {1: 0,2: 1,3: 7,4: 2, 5: 5, 6: 8, 7: 16, 8: 3}

    def getPower(self, n):
        steps = 0
        rem = n % 8
        if rem == 0:
            n = n // 8
            steps = 3
        elif rem == 1:
            n = n // 8 * 9 + 2
            steps = 5
        elif rem == 2:
            n = n // 8 * 3 + 1
            steps = 4
        elif rem == 3:
            n = n // 8 * 9 + 4
            steps = 5
        elif rem == 4 or rem == 5:
            n = n // 8 * 3 + 2
            steps = 4
        elif rem == 6:
            n = n // 8 * 9 + 8
            steps = 5
        else:
            n = n // 8 * 27 + 26
            steps = 6
        # if n in self.cache.keys(): 
        if n <= 8:
            return self.cache[n] + steps
        else:
            return self.getPower(n) + steps

    def getKth(self, low, high, k):
        data = [self.getPower(i) for i in range(low, high + 1)]
        sorted_data = sorted(zip(data, list(range(len(data)))), key= lambda x:x[0])
        return sorted_data[k - 1][1] + low

