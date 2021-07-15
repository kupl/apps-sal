class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        k = min(k,n-1)
        arr = deque(arr)
        win_count = 0
        while True:
            a = arr.popleft()
            b = arr.popleft()
            
            if a > b :
                win_count += 1
                arr.appendleft(a)
                arr.append(b)
            
            else:
                win_count = 1
                arr.appendleft(b)
                arr.append(a)
            if win_count == k:
                return arr[0]                

