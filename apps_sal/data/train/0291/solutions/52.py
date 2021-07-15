class Solution:
    # brute force：把所有的substring都for一遍，可以用bit operation优化
    # 其实不用两个数相加再整除2，直接看最后一位是不是1就行，可以用xor代替相加
    # better approach：对于每个index i，维护evens和odds，分别是在i之前的even prefix sum和odd prefix sum数量，然后用位运算优化
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ret = 0
        # 当前是odd和是even的prefix sums个数
        odds, evens = 0, 1
        cur = 0 # 当前的prefix sum
        
        for num in arr:
            cur ^= num&1    # 查看奇偶
            if cur:         # 奇数
                # 如果当前prefix sum是奇数，查看在此之前有多少个偶数的prefix sum
                # 用cur减去之前所有是偶数的prefix sum，都可以得到一段奇数的substring
                ret += evens
                odds += 1
            else:
                # vice versa
                ret += odds
                evens += 1
        
        return ret % (10**9 + 7)
        
        
#     def numOfSubarrays(self, arr: List[int]) -> int:
#         n = len(arr)
#         ret = 0
        
#         presum = [0 for i in range(n)]
#         for i in range(n):
#             presum[i] = (arr[i] + (presum[i-1] if i > 0 else 0))&1
        
#         for i in range(n):
#             for j in range(i, n):
#                 if i == j:
#                     if arr[i]&1: ret += 1
#                 elif not i:
#                     if presum[j]: ret += 1
#                 else:
#                     if presum[j]^presum[i-1]: ret += 1

#         return ret

