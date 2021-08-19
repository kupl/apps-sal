def bfs(arr, i, d, memo):
    if i in memo:
        return memo[i]
    res = 1
    for j in range(max(i - 1, 0), max(i - d - 1, -1), -1):
        if arr[j] >= arr[i]:
            break
        res = max(res, bfs(arr, j, d, memo) + 1)
    for j in range(i + 1, min(i + d + 1, len(arr))):
        if arr[j] >= arr[i]:
            break
        res = max(res, bfs(arr, j, d, memo) + 1)
    memo[i] = res
    return res


class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        memo = dict()
        return max((bfs(arr, i, d, memo) for i in range(len(arr))))
