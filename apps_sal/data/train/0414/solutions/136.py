class Solution:
    
    def swap(self, arr, winner, loser_idx):
        arr.append(arr.pop(loser_idx))
        return arr
    
    def getWinnerOG(self, arr: List[int], k: int) -> int:
        if k > 2*len(arr):
            return max(arr)
        win_counts = {}
        while True:
            winner = arr[0] if arr[0] > arr[1] else arr[1]
            if winner not in win_counts:
                win_counts[winner] = 1
            else:
                win_counts[winner]+=1
            win_count = win_counts[winner]
            if win_count == k:
                return winner
            arr = self.swap(arr, winner=winner,loser_idx = 1 if arr[0] == winner else 0)
            
    def getWinner(self, arr: List[int], k: int) -> int:
        if k > 2*len(arr):
            return max(arr)
        win_counts = {}
        ptr1 = 0
        ptr2 = 1
        while True:
            # print(ptr1, ptr2)
            winner = arr[ptr1] if arr[ptr1] > arr[ptr2] else arr[ptr2]
            if winner not in win_counts:
                win_counts[winner] = 1
            else:
                win_counts[winner]+=1
            win_count = win_counts[winner]
            if win_count == k:
                return winner
            ptr1 = ptr1 if arr[ptr1] > arr[ptr2] else ptr2
            if ptr2 == len(arr)-1:
                ptr2 = 0
            else:
                ptr2+=1
            if ptr2 == ptr1:
                ptr2+=1
