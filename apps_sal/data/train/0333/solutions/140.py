from queue import Queue


def dedup(arr):
    n = len(arr)
    if n <= 2:
        return arr

    ret = [arr[0]]
    is_equal = False
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            if not is_equal:
                is_equal = True
                ret.append(arr[i])
            else:
                ret[-1] = arr[i]
        else:
            ret.append(arr[i])
            is_equal = False
    return ret


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(set(arr)) == len(arr):
            return len(arr) - 1

        arr = dedup(arr)
        memo = defaultdict(list)
        n = len(arr)
        visited = [0] * n
        for i in range(n):
            memo[arr[i]].append(i)

        q = Queue()
        q.put((0, 0))
        visited[0] = 1
        while not q.empty():
            cur, cnt = q.get()
            if cur == n - 1:
                return cnt

            wk = [cur + 1, cur - 1]
            for v in memo[arr[cur]] + wk:
                if -1 < v < n and not visited[v]:
                    q.put((v, cnt + 1))
                    visited[v] = 1
        return 0
