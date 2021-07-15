from collections import defaultdict

class Solution:
    def findLatestStep(self, arr_: List[int], m: int) -> int:
        arr = [a - 1 for a in arr_]
        n = len(arr)
        last_round = -1

        length = defaultdict(int)
        count = defaultdict(int)

        for i, a in enumerate(arr):
            left, right = length[a-1], length[a+1]
            new_length = left + right + 1

            length[a-left] = new_length
            length[a+right] = new_length

            count[new_length] += 1
            count[left] -= 1
            count[right] -= 1

            if count[m] > 0:
                last_round = i + 1
        
        return last_round
        

