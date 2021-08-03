class Solution:
    def helper(self, A, B):
        count = 0
        left = 0
        right = 0
        d = {}

        while right < len(A):
            if A[right] not in d:
                d[A[right]] = 0
            d[A[right]] += 1

            while len(d) > B:
                d[A[left]] -= 1
                if d[A[left]] == 0:
                    d.pop(A[left])
                left += 1

            count += right - left + 1
            right += 1

        return count

    def subarraysWithKDistinct(self, A: List[int], B: int) -> int:
        return self.helper(A, B) - self.helper(A, B - 1)
