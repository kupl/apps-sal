class Solution:
    def canBeMadeSortedByDeletingKElements(self, arr: List[int], k: int) -> bool:
        # k   : 0 1 2 3 4 5 . . .
        # f(k): 0 0 0 0 1 1 1 1 1 1 1 1
        n = len(arr)

        i = 1
        while i < n and arr[i - 1] <= arr[i]:
            i += 1

        j = 1
        while j < n and arr[n - j - 1] <= arr[n - j]:
            j += 1

        if i == n:  # and j == n
            return True

        # i         > k         j
        # -----  # # # # # ------
        # 3 4 5 1 1 2 3 4
        # k = 2

        if i + j + k < n:
            return False

        # k = 3
        # 0 1 2 3 4 5 6

        # k = 3
        #        0 1 2 3 4 5
        # i = 0: - - -
        # i = 1:   - - -

        for start in range(0, n - k + 1):
            left = start
            right = n - left - k
            if left <= i and right <= j and (left == 0 or right == 0 or arr[left - 1] <= arr[n - right]):
                return True

        return False

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        L = 0
        R = len(arr) - 1
        answer = -1

        while L <= R:
            M = (L + R) // 2
            if self.canBeMadeSortedByDeletingKElements(arr, M):
                answer = M
                R = M - 1
            else:
                L = M + 1

        return answer
