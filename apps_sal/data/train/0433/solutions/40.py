class Solution:

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        goal = k * threshold
        cSums = [0 for i in arr]
        c = 0
        for i in range(len(arr)):
            if i == 0:
                cSums[0] = arr[0]
            else:
                cSums[i] = cSums[i - 1] + arr[i]
            if i == k - 1:
                if cSums[i] >= goal:
                    c += 1
            elif i >= k:
                if cSums[i] - cSums[i - k] >= goal:
                    c += 1
        print(cSums)
        return c
