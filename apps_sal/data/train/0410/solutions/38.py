class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        arr = []
        for i in range(lo, hi + 1):
            arr.append([self.getPower(i), i])
        
        arr.sort(key=lambda x: (x[0], x[1]))
        return arr[k - 1][1]
        
    def getPower(self, number: int) -> int:
        count = 0
        
        while number != 1:
            if number % 2 == 1:
                number = 3 * number + 1
            else:
                number //= 2
            count += 1
        
        return count
