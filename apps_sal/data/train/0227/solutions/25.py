class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        start = end = 0
        res = 0
        map = collections.defaultdict(int)
        while end < len(A):
            map[A[end]] += 1
            while end - start + 1 - map[1] > K:
                map[A[start]] -= 1
                start += 1
            res = max(res, end - start + 1)
            end += 1

        return res
