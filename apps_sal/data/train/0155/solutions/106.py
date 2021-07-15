from functools import lru_cache
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        canJumpRight = collections.defaultdict(set)
        deque = collections.deque()
        for i in range(n):
            # print(deque)
            if not deque:
                deque.append(i)
            else:
                if arr[i] < arr[deque[-1]]:
                    deque.append(i)
                else:
                    temp = collections.deque()
                    while deque and arr[deque[-1]] <= arr[i]:
                        curr = deque.pop()
                        # print('pop', curr, deque and i - deque[-1] <= d)
                        if deque and curr - deque[-1] <= d:
                            canJumpRight[deque[-1]].add(curr)
                            for idx in canJumpRight[curr]:
                                if idx-deque[-1]<=d:
                                    canJumpRight[deque[-1]].add(idx)
                    deque.append(i)
        while deque:
            curr = deque.pop()
            if deque and curr - deque[-1] <= d:
                canJumpRight[deque[-1]].add(curr)
                for idx in canJumpRight[curr]:
                    if idx-deque[-1]<=d:
                        canJumpRight[deque[-1]].add(idx)
                # canJump[deque[-1]].update(canJumpRight[curr])
        canJumpLeft = collections.defaultdict(set)
        for i in range(n-1, -1, -1):
            if not deque:
                deque.append(i)
            else:
                if arr[i] < arr[deque[-1]]:
                    deque.append(i)
                else:
                    while deque and arr[deque[-1]] <= arr[i]:
                        curr = deque.pop()
                        if deque and abs(curr - deque[-1]) <= d:
                            canJumpLeft[deque[-1]].add(curr)
                            for idx in canJumpLeft[curr]:
                                if abs(idx-deque[-1])<=d:
                                    canJumpLeft[deque[-1]].add(idx)
                    deque.append(i)
        while deque:
            curr = deque.pop()
            if deque and abs(curr - deque[-1]) <= d:
                canJumpLeft[deque[-1]].add(curr)
                for idx in canJumpLeft[curr]:
                    if abs(idx-deque[-1])<=d:
                        canJumpLeft[deque[-1]].add(idx)
        res = 0
        arr_set = collections.defaultdict(set)
        for i in range(n):
            arr_set[i] = canJumpLeft[i]|canJumpRight[i]
        res = 0
        @lru_cache(None)
        def dfs(curr):
            nonlocal res
            if curr not in arr_set:
                return 1
            local = 0
            for ne in arr_set[curr]:
                local = max(local, dfs(ne))
            res = max(res, local+1)
            return local+1
        for i in range(n):
            dfs(i)
        return res
        

