class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        odd_even_count = [[0,0] for _ in range(len(arr)+1)]
        prefix_odd_sum = [-1 for _ in range(len(arr))]
        cur = 0
        odd_count = 0
        even_count = 0
        for idx in range(len(arr)):
            cur += arr[idx]
            prefix_odd_sum[idx] = cur % 2
            if cur % 2 == 1:
                odd_count += 1
            else:
                even_count += 1
            odd_even_count[idx+1] = (odd_count, even_count)
        
        ans = 0
        for idx in range(len(arr)):
            is_odd = prefix_odd_sum[idx]
            ## odd: add 1 + prefix even count
            if is_odd:
                ans += 1 + odd_even_count[idx][1] 
            ## even: add prefix odd count
            else:
                ans += odd_even_count[idx][0]
        return ans % mod
                

