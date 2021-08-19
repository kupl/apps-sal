class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        if n <= 1:
            return n
        visited = [False for i in range(n)]
        L_neighbor = {}
        R_neighbor = {}
        for i in range(n):
            L_neighbor[i] = i
            R_neighbor[i] = i
        dec = deque()
        dec.append(0)
        for i in range(1, n):
            while len(dec) > 0:
                if dec[0] < i - d:
                    dec.popleft()
                else:
                    break
            while len(dec) > 0:
                if arr[dec[len(dec) - 1]] < arr[i]:
                    dec.pop()
                else:
                    break
            if len(dec) == 0:
                L_neighbor[i] = max(i - d, 0)
                dec.append(i)
            else:
                L_neighbor[i] = max(dec[len(dec) - 1] + 1, i - d, 0)
                dec.append(i)
        dec = deque()
        dec.append(n - 1)
        for i in range(n - 2, -1, -1):
            while len(dec) > 0:
                if dec[0] > i + d:
                    dec.popleft()
                else:
                    break
            while len(dec) > 0:
                if arr[dec[len(dec) - 1]] < arr[i]:
                    dec.pop()
                else:
                    break
            if len(dec) == 0:
                R_neighbor[i] = min(i + d, n - 1)
                dec.append(i)
            else:
                R_neighbor[i] = min(dec[len(dec) - 1] - 1, i + d, n - 1)
                dec.append(i)
        res = 0
        limit = [0 for i in range(n)]
        for i in range(n):
            self.maxJumpDFS(i, arr, L_neighbor, R_neighbor, visited, limit)
        for i in range(n):
            if res < limit[i]:
                res = limit[i]
        return res

    def maxJumpDFS(self, start, arr, L_neighbor, R_neighbor, visited, limit):
        if visited[start]:
            return limit[start]
        else:
            currmax = 0
            for i in range(L_neighbor[start], R_neighbor[start] + 1):
                if i == start:
                    continue
                curr = self.maxJumpDFS(i, arr, L_neighbor, R_neighbor, visited, limit)
                if currmax < curr:
                    currmax = curr
            visited[start] = True
            limit[start] = currmax + 1
            return limit[start]
