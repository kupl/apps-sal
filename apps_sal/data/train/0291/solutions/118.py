class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        mod = 1000000000.0 + 7
        seen = [1, 0]
        for i in range(len(arr)):
            if i > 0:
                arr[i] += arr[i - 1]
            ans += seen[(arr[i] + 1) % 2]
            ans %= mod
            seen[arr[i] % 2] += 1
        return int(ans)
