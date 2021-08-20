class Solution:

    def longestMountain(self, A: List[int]) -> int:
        left = right = 0
        max_length = 0
        while left < len(A):
            prev = A[left]
            climbing = False
            descending = False
            right = left + 1
            while right < len(A):
                current = A[right]
                if prev < current and (not descending):
                    climbing = True
                elif prev > current and (climbing or descending):
                    climbing = False
                    descending = True
                else:
                    right -= 1
                    break
                right += 1
                prev = current
            if right == len(A):
                right -= 1
            curr_length = right - left + 1
            if curr_length > 2 and descending:
                max_length = max(max_length, curr_length)
            left = max(left + 1, right)
        return max_length
