class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = odd = even = 0
        for i in arr:
            if i % 2 == 0:
                even, odd = even + 1, odd
            else:
                even, odd = odd, even + 1
            ans = (ans + odd) % 1000000007
        return ans
        '''
        ans=0
        for i in range (len(arr)):
            temp=0
            for j in range(i,len(arr)):
                temp+=arr[j]
                if temp%2==1:
                    ans+=1
        return ans%1000000007
        '''
