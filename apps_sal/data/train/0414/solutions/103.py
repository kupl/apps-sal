class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if (k > len(arr)):
            return max(arr)
        win = {arr[0]:0,arr[1]:0}
        while(win[arr[0]] < k and win[arr[1]] < k):
            if (arr[0]>arr[1]):
                win[arr[0]] = win[arr[0]] + 1   
                arr.append(arr[1])
                arr.remove(arr[1])
            else:
                win[arr[1]] = win[arr[1]] + 1
                arr.append(arr[0])
                arr.remove(arr[0])
            win[arr[1]] = 0
        if(win[arr[0]]==k):
            return arr[0]
        else:
            return arr[1]

