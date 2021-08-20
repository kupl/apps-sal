class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        nums = {}
        for (i, num) in enumerate(A):
            nums[num] = i

        def dfs(prev, cur, visit):
            if (prev, cur) in visit:
                return visit[prev, cur]
            if prev == -1:
                res = 0
                for i in range(len(A)):
                    for j in range(i + 1, len(A)):
                        if A[i] + A[j] in nums:
                            res = max(res, 1 + dfs(i, j, visit))
                return res
            if A[prev] + A[cur] in nums:
                visit[prev, cur] = 1 + dfs(cur, nums[A[prev] + A[cur]], visit)
            else:
                visit[prev, cur] = 1
            return visit[prev, cur]
        return dfs(-1, -1, {})
