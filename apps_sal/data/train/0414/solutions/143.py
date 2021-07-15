class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        current_num = arr[0]
        count = 0
        for i in range(1, len(arr)):
            if current_num > arr[i]:
                count += 1
            else:
                current_num = arr[i]
                count = 1
            if count == k:
                    break

        return current_num

