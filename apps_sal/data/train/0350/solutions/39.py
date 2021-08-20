class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        def helper(A, K):
            d = defaultdict(int)
            begin = 0
            end = 0
            ans = float('-inf')
            count = 0
            res = 0
            while end < len(A):
                char = A[end]
                d[char] += 1
                if d[char] == 1:
                    count += 1
                end += 1
                while count > K:
                    temp = A[begin]
                    d[temp] -= 1
                    if d[temp] == 0:
                        count -= 1
                    begin += 1
                res += end - begin + 1
            return res
        return helper(A, K) - helper(A, K - 1)
