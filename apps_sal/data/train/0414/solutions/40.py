class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        if k > len(arr) // 2:
            return max(arr)
        nums = 0
        while nums < k:
            if arr[0] < arr[1]:
                nums = 1
                arr.append(arr.pop(0))
            else:
                nums += 1
                arr.append(arr.pop(1))
        return arr[0]
