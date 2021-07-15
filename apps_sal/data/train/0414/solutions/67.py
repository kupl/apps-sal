class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        count = 0
        prev = 0
        i=0
        len_arr = len(arr)
        while count < k:
            if i > len_arr:
                return arr[0]
            if arr[0] > arr[1]:
                if arr[0] == prev:
                    count +=1
                prev = arr[0]
                arr.append(arr[1])
                arr.pop(1)
            elif arr[1] > arr[0]:
                count = 1
                prev = arr[1]
                arr.append(arr[0])
                arr.pop(0)
            i+=1
        return arr[0]        
