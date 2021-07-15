class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        self.dp = {}
        self.arr = A
        ans = self.helper(0,K-1)
        #print(self.dp)
        return ans
        
    
    def helper(self,i,k):
        if(k == 0):
            return sum(self.arr[i:])/len(self.arr[i:])
        if(i == len(self.arr)-1):
            return -10**100
        
        if((i,k) in self.dp):
            return self.dp[(i,k)]
        
        ans = 0
        for j in range(i,len(self.arr)-1):
            tmp = sum(self.arr[i:j+1])/(len(self.arr[i:j+1])) + self.helper(j+1, k-1)
            ans = max(ans, tmp)
        self.dp[(i,k)] = ans
        return self.dp[(i,k)]

