
class Solution:
    cache = {}
    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        l = list(range(lo, hi + 1))
        l.sort(key = lambda x: self.findKth(x))
        return l[k - 1]
        
    # 牛啤的recursion + cache优化
    def findKth(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        
        if n == 1:
            return 0
        
        if n % 2 == 0:
            res = 1 + self.findKth(int(n / 2))
        else:
            res = 1 + self.findKth(3 * n + 1)
            
        self.cache[n] = res
        return res


class Solution_eva:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        def calSteps(x):
            cnt = 0
            # O(n)
            while x != 1:
                x = x / 2 if x % 2 == 0 else 3*x + 1
                cnt += 1
            return cnt
        # O(nlogn) * O(n)
        return sorted([ele for ele in range(lo, hi+1)], key=lambda x: calSteps(x))[k-1]

