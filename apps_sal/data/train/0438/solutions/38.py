class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        
        startwith = dict()
        endwith = dict()
        length = dict()
        ans = -1
        for i in range(len(arr)):
            if arr[i]+1 in startwith:
                if arr[i]-1 in endwith:
                    new_start = endwith[arr[i]-1]
                    new_end = startwith[arr[i]+1]
                    old_start = endwith[arr[i]-1]
                    old_end = arr[i]-1
                    del endwith[arr[i]-1]
                    length[old_end - old_start + 1] -= 1
                else:
                    new_start = arr[i]
                    new_end = startwith[arr[i]+1]
                old_start = arr[i]+1
                old_end = startwith[arr[i]+1]
                del startwith[arr[i]+1]
                length[old_end - old_start + 1] -= 1 
            elif arr[i]-1 in endwith:
                new_start = endwith[arr[i]-1]
                new_end = arr[i]
                old_start = endwith[arr[i]-1]
                old_end = arr[i]-1             
                length[old_end - old_start + 1] -= 1
                del endwith[arr[i]-1]
            else:
                new_start = arr[i]
                new_end = arr[i]
            length[new_end - new_start + 1] = length.get(new_end - new_start + 1, 0) + 1
            startwith[new_start] = new_end
            endwith[new_end] = new_start
            if m in length and length[m] > 0: ans = i+1
        return ans

