class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        que = collections.deque([(1, n)])
        for i in range(n - 1, -1, -1):
            k = len(que)
            for j in range(k):
                (l, r) = que.popleft()
                if r - l + 1 == m:
                    return i + 1
                if l <= arr[i] <= r:
                    if arr[i] - l >= m:
                        que.append((l, arr[i] - 1))
                    if r - arr[i] >= m:
                        que.append((arr[i] + 1, r))
                else:
                    que.append((l, r))
        return -1
