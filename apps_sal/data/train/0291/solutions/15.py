class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        mod = 10**9+7
        ans = 0
        p = [0]*(n+1)
        counter = Counter([0]) 
        for i in range(n):
            p[i] = p[i-1]+arr[i]
            if p[i]%2: ans += counter[0]
            else: ans += counter[1]
            counter[p[i]%2] += 1
        return ans%mod
