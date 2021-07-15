class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dic = {}
        for x in range(lo, hi+1):
            dic[x] = self.get_power(x, 0)
        dic_2 = {k: dic[k] for k in sorted(dic, key=dic.get)}
        return list(dic_2.keys())[k-1]
    def get_power(self, x:int, p:int) -> int:
        while x!=1:
            if x%2==0:
                x//=2
            else:
                x = 3*x+1
            p+=1
        return p

