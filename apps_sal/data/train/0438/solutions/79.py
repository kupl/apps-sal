class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m > len(arr):
            return -1
        elif m == len(arr):
            return len(arr)
        else:
            pass
        bit_information = [0] * (len(arr) + 1)
        target_group_size_counter = 0
        ret = -2
        for i in range(len(arr)):
            group_sizes = []
            total_length = 1
            neighbor_group_exists = [False, False]
            if arr[i] > 1 and bit_information[arr[i] - 1] != 0:
                total_length += bit_information[arr[i] - 1]
                neighbor_group_exists[0] = True
            if arr[i] < len(arr) and bit_information[arr[i] + 1] != 0:
                total_length += bit_information[arr[i] + 1]
                neighbor_group_exists[1] = True
            bit_information[arr[i]] = total_length
            if neighbor_group_exists[0]:
                target_group_size_counter -= 1 if bit_information[arr[i] - 1] == m else 0
                bit_information[arr[i] - bit_information[arr[i] - 1]] = total_length
            if neighbor_group_exists[1]:
                target_group_size_counter -= 1 if bit_information[arr[i] + 1] == m else 0
                bit_information[arr[i] + bit_information[arr[i] + 1]] = total_length
            target_group_size_counter += 1 if total_length == m else 0
            ret = i if target_group_size_counter > 0 else ret
        return ret + 1
