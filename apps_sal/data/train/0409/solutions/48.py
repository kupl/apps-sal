class Solution:

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:

        def find_max(A):
            start = 0
            curr = 0
            res = 0
            for end in range(len(A)):
                curr += A[end]
                while curr < 0:
                    curr -= A[start]
                    start += 1
                res = max(res, curr)
            return res
        if all((i <= 0 for i in arr)):
            return 0
        if k == 1:
            return find_max(arr)
        res = max(find_max(arr), find_max(arr + arr), sum(arr) * k, find_max(arr + arr) + sum(arr) * (k - 2))
        return res % (10 ** 9 + 7)
