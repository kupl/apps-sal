class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sm = threshold * k
        ct = 0
        tot = 0
        for i in range(len(arr)):
            tot += arr[i]
            if i < k - 1: continue
            if i > k - 1: tot -= arr[i - k]
            if tot >= sm: ct += 1
        return ct
            

