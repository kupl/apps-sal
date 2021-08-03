class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        ans = float('inf')
        max_s, min_e = 0, n - 1
        curr = -1
        for i, a in enumerate(arr):
            if a < curr:
                break
            curr = a
            max_s = i

        curr = float('inf')
        for i in range(n - 1, -1, -1):
            if arr[i] > curr:
                break
            curr = arr[i]
            min_e = i
        # n - 1 - (max_s + 1) + 1 = n - 1 - max_ s
        # min_e - 1 - 0 + 1 = min_e
        ans = min(n - max_s - 1, min_e)

        for s in range(max_s + 1):
            index, jump = n - 1, n - 1
            while jump >= 1:
                while index - jump >= min_e and arr[index - jump] >= arr[s]:
                    index -= jump
                jump //= 2
            if index > s and arr[index] >= arr[s]:
                ans = min(ans, index - 1 - (s + 1) + 1)
        return ans
