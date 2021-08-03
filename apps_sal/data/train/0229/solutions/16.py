class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        A.sort(key=lambda x: (x > 0, abs(x)))
        right = 1
        size = len(A)
        for i in range(size):
            if A[i] is None:
                continue

            while right < size and 2 * A[i] != A[right]:
                right += 1

            if right == size:
                return False

            A[right] = None

        return True
