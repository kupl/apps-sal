class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        '''
        This is an elementary dynamic programming problem.
        odd[i] records the number of subarray ending at arr[i] that has odd sum.
        even[i] records the number of subarray ending at arr[i] that has even sum.
        if arr[i + 1] is odd, odd[i + 1] = even[i] + 1 and even[i + 1] = odd[i]
        if arr[i + 1] is even, odd[i + 1] = odd[i] and even[i + 1] = even[i] + 1
        Since we only required the previous value in odd and even, we only need O(1) space.
        '''
        res = odd = even = 0
        for x in arr:
            even += 1
            if x % 2:
                odd, even = even, odd
            res = (res + odd) % 1000000007             
        return res
