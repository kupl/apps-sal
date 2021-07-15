class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power(x):
            count = 0
            while x > 1:
                if x % 2:
                    x = 3* x + 1
                else:
                    x = x /2
                count +=1
            return count
        return sorted(range(lo,hi+1), key=power)[k-1]
