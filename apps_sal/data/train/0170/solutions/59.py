class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        pointer1 = -1
        n = len(arr)
        pointer2 = n - 1
        for i in range(n - 2, 0, -1):
            if arr[i] > arr[i + 1]:
                break
            pointer2 = i
        res = pointer2 - pointer1 - 1
        for pointer1 in range(n):
            if pointer1 > 0 and arr[pointer1] < arr[pointer1 - 1]:
                break
            while(pointer2 < n and (pointer2 <= pointer1 or arr[pointer2] < arr[pointer1])):
                pointer2 += 1
            res = min(res, pointer2 - pointer1 - 1)
        return res
