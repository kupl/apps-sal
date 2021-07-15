
    

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        count = [0] * (n+1)
        length = [0] * ( n + 2)
        ans = -1
        for i,v in enumerate(arr):
            left = length[v - 1]
            right = length[v + 1]
            length[v] = length[v - left] = length[v + right] = left + right + 1
            count[left] -= 1
            count[right] -= 1
            count[length[v]] += 1
            if count[m] >0:
                ans = i + 1
            
        return ans
            
        

