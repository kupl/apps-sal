class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        # HashMap
        # count = {0:1}
        # presum = res = 0
        # for num in A:
        #     presum += num
        #     if presum - S in count:
        #         res += count[presum - S]
        #     count[presum] = count.get(presum, 0) + 1
        # return res
        
        # two pointers
        # def atMost(k):
        #     n = len(A)
        #     left = presum = res = 0
        #     for right in range(n):
        #         presum += A[right]
        #         while left <= right and presum > k:
        #             presum -= A[left]
        #             left += 1
        #         res += right - left + 1
        #     return res
        # return atMost(S) - atMost(S - 1)
        
        left = res = cur_sum = count = 0
        for right in range(len(A)):
            cur_sum += A[right]
            if A[right] == 1:
                count = 0
            while left <= right and cur_sum >= S:
                if cur_sum == S:
                    count += 1
                cur_sum -= A[left]
                left += 1
            res += count
        return res
