class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        arr = [-float('inf')] + arr + [float('inf')]
        sorted_to = [False for _ in range(len(arr))]
        sorted_from = [False for _ in range(len(arr))]
        rev_arr = arr[::-1]
        last_sorted_to = -1
        first_sorted_from = -1
        shortest = float('inf')
        for (idx, val) in enumerate(arr):
            if idx == 0 or val >= arr[idx - 1]:
                sorted_to[idx] = True
                last_sorted_to = idx
            else:
                break
        for (idx, val) in enumerate(rev_arr):
            if idx == 0 or val <= rev_arr[idx - 1]:
                sorted_from[len(arr) - 1 - idx] = True
                first_sorted_from = len(arr) - 1 - idx
            else:
                break
        if arr == sorted(arr):
            return 0
        for i in range(last_sorted_to + 1):
            for j in range(first_sorted_from, len(arr)):
                if arr[j] >= arr[i]:
                    shortest = min(shortest, j - i - 1)
                    break
            shortest = min(shortest, len(arr) - i - 1)
        return shortest
