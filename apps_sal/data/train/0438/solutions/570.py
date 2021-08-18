class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        latest = -1

        if len(arr) == 1:
            return 1 if arr[0] == m else -1

        length_count = [0 for _ in range(len(arr) + 1)]
        binary_str = [0 for _ in range(len(arr))]
        for idx in range(len(arr)):
            num = arr[idx] - 1
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

            if length_count[m] > 0:
                latest = idx

        return latest + 1 if latest > -1 else -1
