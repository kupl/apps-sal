class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        length = [0]*(len(arr)+2)
        count = [0]*(len(arr)+1)
        latest = -1
        for idx, pos in enumerate(arr):
            left, right = length[pos-1], length[pos+1]
            length[pos] = length[pos - left] = length[pos + right] = left + right + 1
            count[left] -= 1
            count[right] -= 1
            count[length[pos]] += 1
            if count[m]:
                latest = idx + 1
        return latest

                
                
                

