class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd, even = 0, 0
        arr = [i % 2 for i in arr]

        if arr[0] != 0:
            odd += 1
        else:
            even += 1

        for i in range(1, len(arr)):
            arr[i] = arr[i - 1] + arr[i]
            if arr[i] % 2 == 0:
                even += 1
            else:
                odd += 1

        ans = 0
        for i in arr[::-1]:
            if i % 2 == 0 and odd > 0:
                ans += odd
                even -= 1
            elif i % 2 == 1:
                ans += (even + 1)
                odd -= 1
            else:
                continue
        return ans % (10**9 + 7)
