class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        even = [0] * len(arr)
        odd = [0] * len(arr)
        for i in range(len(arr)):
            if i == 0 and arr[i] % 2 == 0:
                even[i] = 1
            elif i == 0:
                odd[i] = 1
            elif arr[i] % 2 == 0:
                even[i] = even[i - 1] + 1
                odd[i] = odd[i - 1]
            else:
                even[i] = odd[i - 1]
                odd[i] = even[i - 1] + 1
        mod = 10 ** 9 + 7
        ans = 0
        for i in range(len(arr)):
            ans = (ans + odd[i]) % mod
        return ans
