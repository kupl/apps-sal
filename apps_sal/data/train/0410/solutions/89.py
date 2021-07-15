class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def get_power(x:int, p:int) -> int:
            while x != 1:
                x = x //2 if x %2 == 0 else (3 * x) + 1
                p += 1
            return p
        
        dic = { x: get_power(x, 0) for x in range(lo, hi+1) }
        return sorted(list(dic.items()), key=lambda x: x[1])[k-1][0]


