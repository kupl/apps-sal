class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = odd = even = 0
        for i in arr:
            if i % 2 == 0:
                (even, odd) = (even + 1, odd)
            else:
                (even, odd) = (odd, even + 1)
            ans = (ans + odd) % 1000000007
        return ans
        '\n        ans=0\n        for i in range (len(arr)):\n            temp=0\n            for j in range(i,len(arr)):\n                temp+=arr[j]\n                if temp%2==1:\n                    ans+=1\n        return ans%1000000007\n        '
