from collections import defaultdict


class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        memo = defaultdict(int)
        visited = dict()
        visited[A[0]] = True
        visited[A[1]] = True
        ret = 0
        for i in range(2, len(A)):
            num = A[i]
            visited[num] = True
            for j in range(i - 1, -1, -1):
                if num - A[j] in visited and num - A[j] < A[j]:
                    old_key = (num - A[j], A[j])
                    val = memo[old_key] + 1
                    ret = max(ret, val)
                    key = (A[j], num)
                    memo[key] = val
        if ret:
            ret += 2
        return ret
