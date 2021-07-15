class Solution:
    def knightDialer(self, n: int) -> int:
        if n ==1:return 10
        f1,f2,f3,f4,f6,f7,f8,f9,f0 = [1]*n,[1]*n,[1]*n,[1]*n,[1]*n,[1]*n,[1]*n,[1]*n,[1]*n
        
        for j in range(1,n):
            f0[j] = (f4[j-1]+f6[j-1])%(1e9+7)
            f1[j] = (f6[j-1]+f8[j-1])%(1e9+7)
            f2[j] = (f7[j-1]+f9[j-1])%(1e9+7)
            f3[j] = (f4[j-1]+f8[j-1])%(1e9+7)
            f4[j] = (f3[j-1]+f9[j-1]+f0[j-1])%(1e9+7)
            f6[j] = (f1[j-1]+f7[j-1]+f0[j-1])%(1e9+7)
            f7[j] = (f6[j-1]+f2[j-1])%(1e9+7)
            f8[j] = (f1[j-1]+f3[j-1])%(1e9+7)
            f9[j] = (f2[j-1]+f4[j-1])%(1e9+7)
        
        # res = 2*(f0[n]+f1[n]+f2[n]+f3[n]+f7[n]+f8[n]+f9[n])+3*(f4[n]+f6[n])
        res = f0[n-1]+f1[n-1]+f2[n-1]+f3[n-1]+f7[n-1]+f8[n-1]+f9[n-1]+f4[n-1]+f6[n-1]
        return int(res%(1e9+7))
