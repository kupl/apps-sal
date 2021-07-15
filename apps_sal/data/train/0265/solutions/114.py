class Solution:
    def maxNonOverlapping(self, A: List[int], target: int) -> int:
        
        # dp[i + 1] = Math.max(dp[i + 1], dp[j] + (sum == target ? 1 : 0));
        # a = [0] * (len(A) + 1)
        # for i in range (len(A)):
        #     sums = 0
        #     for j in reversed(range(i + 1)):
        #         sums += A[j]
        #         a[i + 1] = max(a[i + 1], a[j] + 1 if sums == target else 0)
        # print(a)
        # return a[len(A)]
        
        seen = {0}
        prefix_sum = count = 0
        
        for a in A:
            prefix_sum += a
            if -target + prefix_sum in seen:
                prefix_sum = 0
                count += 1
                seen = set()
            seen.add(prefix_sum)    
            
        return count
            

