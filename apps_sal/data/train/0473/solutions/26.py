# N = len(arr)
# time: O(N^2)
# space: O(N^2)
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        memo = [arr[:] for _ in range(len(arr))]
        for i in range(len(arr)):
            tmp = arr[i]
            for j in range(i + 1, len(arr)):
                tmp ^= arr[j]
                memo[i][j] = tmp
        return sum([(j - i) * (memo[i][j] == 0) for i in range(len(arr)) for j in range(i + 1, len(arr))])

