class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:

        arr = sorted(arr, reverse=True)
        print(arr)
        for i in range(len(arr) - 1, -1, -1):

            sol = round(target / (i + 1))

            if arr[i] >= sol:
                return sol
            target -= arr[i]
            
        return arr[0]
                


