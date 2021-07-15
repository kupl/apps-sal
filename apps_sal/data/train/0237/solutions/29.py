class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        # n = len(A)
        # l = 0
        # sums = 0
        # add = 1
        # ans = 0
        # for r in range(n):
        #     sums += A[r]
        #     while sums > S or A[l] == 0:
        #         if sums > S:
        #             add = 1
        #         else:
        #             add += 1
        #         sums -= A[l]
        #         l += 1
        #     if sums == S:
        #         ans += add
        # return ans
        
        hashmap = {0:1}
        preSum = 0
        ans = 0
        for i in range(len(A)):
            preSum += A[i]
            if preSum - S in hashmap:
                ans += hashmap[preSum -S]
            hashmap[preSum] = 1 if preSum not in hashmap else hashmap[preSum] + 1
        return ans
            

