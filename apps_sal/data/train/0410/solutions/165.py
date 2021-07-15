class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dic = {}
        for i in range(lo,hi+1):
            power = self.findPower(i,{})
            dic[i] = power
        #print(dic)
        sortedValue = sorted(list(dic.items()), key=lambda x:x[1])
        return (sortedValue[k-1][0])
    
    def findPower(self,num,memo):
        if num in memo:
            return memo[num]
        if num == 1:
            return 1
        memo[num]=self.findPower(num//2,memo)+1 if num % 2 == 0 else self.findPower(3*num+1, memo)+1
        return memo[num]

