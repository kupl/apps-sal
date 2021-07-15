class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k == 1:
            return max(arr[0], arr[1])
        if k >= len(arr) - 1:
            return max(arr)
        count = 0
        result = arr[0]
        while count < k:
            # Move second entry to back.
            if arr[0] > arr[1]:
                count += 1
                arr.append(arr.pop(1))
            else:
                arr.append(arr.pop(0))
                # Set count back to 1 to account for first win for second entry.
                count = 1
                result = arr[0]
        return result
                
            
            

