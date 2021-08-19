import collections


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque = collections.deque()
        max_deque = collections.deque()
        longest_subarray = 0

        i, j = 0, 0
        min_deque.append((nums[0], 0))
        max_deque.append((-nums[0], 0))

        while j < len(nums) and len(nums) - i + 1 > longest_subarray:
            # Remove elements from the min and max that are stale
            while min_deque and min_deque[0][1] < i:
                min_deque.popleft()
            while max_deque and max_deque[0][1] < i:
                max_deque.popleft()

            # Keep adding elements if the invariant is true
            while i > j or (j < len(nums) - 1 and (max(-max_deque[0][0], nums[j + 1]) - min(min_deque[0][0], nums[j + 1]) <= limit)):
                j += 1
                self.insert_to_deque(min_deque, nums[j], j)
                self.insert_to_deque(max_deque, -nums[j], j)

            longest_subarray = max(longest_subarray, j - i + 1)
            i += 1

        return longest_subarray

    def insert_to_deque(self, deque_object, value, index):
        # Keep popping from the right until the new value is smaller
        while len(deque_object) > 0 and deque_object[-1][0] >= value:
            deque_object.pop()
        deque_object.append((value, index))
