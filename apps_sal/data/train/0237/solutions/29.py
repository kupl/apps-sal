class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:

        hashmap = {0: 1}
        preSum = 0
        ans = 0
        for i in range(len(A)):
            preSum += A[i]
            if preSum - S in hashmap:
                ans += hashmap[preSum - S]
            hashmap[preSum] = 1 if preSum not in hashmap else hashmap[preSum] + 1
        return ans
