class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        latest = -1

        if len(arr) == 1:
            return 1 if arr[0] == m else -1

        # (length -> appear times)
        length_count = [0 for _ in range(len(arr) + 1)]
        # store consecutive 1's count ((start, end) -> length)
        binary_str = [0 for _ in range(len(arr))]
        for idx in range(len(arr)):
            num = arr[idx] - 1
            # left boundary
            if num <= 0:
                if binary_str[num + 1] > 0:
                    right_count = binary_str[num + 1]
                    binary_str[num] = 1 + right_count
                    binary_str[num + right_count] += 1
                    length_count[1 + right_count] += 1
                    length_count[right_count] -= 1
                else:
                    binary_str[num] = 1
                    length_count[1] += 1
            # right boundary
            elif num >= len(arr) - 1:
                if binary_str[num - 1] > 0:
                    left_count = binary_str[num - 1]
                    binary_str[num - left_count] += 1
                    binary_str[num] = 1 + left_count
                    length_count[1 + left_count] += 1
                    length_count[left_count] -= 1
                else:
                    binary_str[num] = 1
                    length_count[1] += 1
            # in the middle
            else:
                if binary_str[num + 1] > 0 and binary_str[num - 1] > 0:
                    left_count = binary_str[num - 1]
                    right_count = binary_str[num + 1]
                    binary_str[num - left_count] += (right_count + 1)
                    binary_str[num + right_count] += (left_count + 1)
                    length_count[left_count + right_count + 1] += 1
                    length_count[left_count] -= 1
                    length_count[right_count] -= 1
                elif binary_str[num + 1] > 0 and binary_str[num - 1] <= 0:
                    right_count = binary_str[num + 1]
                    binary_str[num] = 1 + right_count
                    binary_str[num + right_count] += 1
                    length_count[1 + right_count] += 1
                    length_count[right_count] -= 1
                elif binary_str[num + 1] <= 0 and binary_str[num - 1] > 0:
                    left_count = binary_str[num - 1]
                    binary_str[num - left_count] += 1
                    binary_str[num] = 1 + left_count
                    length_count[1 + left_count] += 1
                    length_count[left_count] -= 1
                else:
                    binary_str[num] = 1
                    length_count[1] += 1

            #print(num, binary_str, latest, idx, length_count)
            if length_count[m] > 0:
                latest = idx

        return latest + 1 if latest > -1 else -1
