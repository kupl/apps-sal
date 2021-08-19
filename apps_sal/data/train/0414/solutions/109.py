class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        maxv = max(arr)
        queue = collections.deque(arr)
        c = 0
        w = queue[0]
        while queue[0] != maxv:
            a, b = queue.popleft(), queue.popleft()
            # print(a, b)
            if a < b:
                queue.append(a)
                queue.appendleft(b)
            else:
                queue.append(b)
                queue.appendleft(a)
            if queue[0] == w:
                c += 1
            else:
                c = 1
                w = queue[0]
            if c == k:
                return w
        return maxv
