class Solution:

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k:
            return 0
        store = [0] * len(arr)
        i = 0
        j = 0
        ans = 0
        while i < len(arr):
            if i - j + 1 == k:
                if j == 0:
                    store[i] = store[i - 1] + arr[i]
                else:
                    store[i] = store[i - 1] + arr[i] - arr[j - 1]
                if store[i] // k >= threshold:
                    ans = ans + 1
                j = j + 1
                i = i + 1
            else:
                if i == 0:
                    store[i] = arr[i]
                else:
                    store[i] = arr[i] + store[i - 1]
                i = i + 1
        return ans
