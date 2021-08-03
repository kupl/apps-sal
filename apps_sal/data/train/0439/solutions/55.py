class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:

        longest = 1
        i, start = 0, 0
        t = None

        while i < len(A) - 1:
            while i < len(A) - 1:
                t = self.turType(A, i)
                if t is not None:
                    start = i
                    i += 1
                    break
                i += 1

            while i < len(A) - 1:
                if self.turType(A, i) == t:
                    i += 1
                    if i == len(A) - 1:
                        longest = max(longest, i - start + 1)
                        break
                else:
                    print(longest, t, i, start)
                    longest = max(longest, i - start + 1)
                    break
        return longest

    def turType(self, A: List[int], k: int) -> str:
        if k + 1 >= len(A):
            return None
        is_odd = k % 2 == 1
        if (is_odd and A[k] > A[k + 1]) or (not is_odd and A[k] < A[k + 1]):
            return 'odd'
        if (is_odd and A[k] < A[k + 1]) or (not is_odd and A[k] > A[k + 1]):
            return 'eve'
        return None
