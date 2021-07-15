import collections
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        dq = collections.deque(arr)
        
        conseq = 0
        curr_win = None
        while conseq < k:
            a, b = dq.popleft(), dq.popleft()
            
            maxAB = max(a, b)
            minAB = min(a, b)
            
            if maxAB == curr_win:
                conseq += 1
            else:
                conseq = 1
                curr_win = maxAB
                
            dq.appendleft(maxAB)
            dq.append(minAB)
            
            if conseq == k:
                return curr_win
            
            if conseq > len(arr):
                return curr_win
