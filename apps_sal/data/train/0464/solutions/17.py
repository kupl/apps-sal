class Solution:
    def minOperations(self, n: int) -> int:
        ans=0
        for i in range(1,2*n,2):
            ans+=abs(i-n)
        return ans>>1
