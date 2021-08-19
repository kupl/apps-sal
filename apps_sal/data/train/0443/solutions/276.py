class Solution:
    def numTeams(self, rating: List[int]) -> int:

        # s1: recursive approach, needs to be made into dp

        def solve(arr, n, k, arr_max):

            # base condition
            if k == 0:
                return 1

            if n == len(arr):
                return 0

            # recursive logic
            if arr[n] > arr_max:
                return solve(arr, n + 1, k - 1, arr[n]) + solve(arr, n + 1, k, arr_max)
            else:
                return solve(arr, n + 1, k, arr_max)

        return solve(rating, 0, 3, 0) + solve(rating[::-1], 0, 3, 0)
