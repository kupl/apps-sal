class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        turns = 0
        if k > len(arr):
            return max(arr)
        while turns < k:
            first = arr[0]
            second = arr[1]
            if first < second:
                del arr[0]
                arr.append(first)
                turns = 1
            else:
                del arr[1]
                arr.append(second)
                turns += 1
        return arr[0]
