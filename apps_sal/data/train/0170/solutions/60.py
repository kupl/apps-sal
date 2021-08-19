class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        (leftIncreasing, rightDecreasing) = (1, 1)
        for (left, right) in zip(arr, arr[1:]):
            if left <= right:
                leftIncreasing += 1
            else:
                break
        for (right, left) in zip(arr[::-1], arr[::-1][1:]):
            if left <= right:
                rightDecreasing += 1
            else:
                break
        if max(leftIncreasing, rightDecreasing) == len(arr):
            return 0
        else:
            (left_candidate, right_candidate) = (0, len(arr) - rightDecreasing)
            max_crop_length = max(leftIncreasing, rightDecreasing)
            if max_crop_length == leftIncreasing:
                (crop_start, crop_end) = (leftIncreasing, len(arr) - 1)
            else:
                (crop_start, crop_end) = (0, len(arr) - rightDecreasing - 1)
            while left_candidate < leftIncreasing and right_candidate < len(arr):
                if arr[left_candidate] > arr[right_candidate]:
                    while right_candidate < len(arr):
                        if arr[left_candidate] > arr[right_candidate]:
                            right_candidate += 1
                        else:
                            break
                    if right_candidate == len(arr):
                        return len(arr[crop_start:crop_end + 1])
                    elif max_crop_length < left_candidate + 1 + (len(arr) - right_candidate):
                        (crop_start, crop_end) = (left_candidate + 1, right_candidate - 1)
                        max_crop_length = left_candidate + 1 + (len(arr) - right_candidate)
                else:
                    if max_crop_length < left_candidate + 1 + (len(arr) - right_candidate):
                        (crop_start, crop_end) = (left_candidate + 1, right_candidate - 1)
                        max_crop_length = left_candidate + 1 + (len(arr) - right_candidate)
                    left_candidate += 1
            return len(arr[crop_start:crop_end + 1])
