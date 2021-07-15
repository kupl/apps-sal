class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        def getPower(x):
            count = 0
            while x != 1:
                if x % 2 == 0:
                    x = x // 2
                else:
                    x = 3 * x + 1
                count += 1
            return count
        
        output = [[getPower(x), x] for x in range(lo, hi + 1)]
        output.sort(key = lambda x: (x[0], x[1]))
        return output[k-1][1]
