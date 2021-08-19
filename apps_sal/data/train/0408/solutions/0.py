class Solution:

    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        for i in range(n):
            sol = round(target / n)
            if arr[i] >= sol:
                return sol
            target -= arr[i]
            n -= 1
        return arr[-1]
