class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        # the cost of remove a is a * b b >= a. Greedy using the smallest b in the rest to time a to minimize the cost
        while len(arr) > 1:
            i = arr.index(min(arr))
            res += min(arr[i - 1:i] + arr[i + 1:i + 2]) * arr.pop(i)

        return res
