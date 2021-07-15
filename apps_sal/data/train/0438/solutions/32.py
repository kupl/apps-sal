class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        length_at_index = [0]*(len(arr)+2)
        count_of_length = [0]*(len(arr)+1)
        res = -1
        for i,index in enumerate(arr):
            left_length = length_at_index[index-1]
            right_length = length_at_index[index+1]

            new_length = left_length + right_length + 1
            length_at_index[index] = new_length
            length_at_index[index-left_length] = new_length
            length_at_index[index+right_length] = new_length

            count_of_length[left_length] -= 1
            count_of_length[right_length] -= 1
            count_of_length[new_length] += 1

            if count_of_length[m] > 0:res = i+1
        return res
