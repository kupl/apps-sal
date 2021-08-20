class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        running = [0]
        for num in A:
            running.append(running[-1] + num)
        result = math.inf
        deque = collections.deque([0])
        r = 1
        while r < len(running):
            if not deque:
                deque.append(r)
                r += 1
                continue
            while deque and r < len(running) and (running[r] - running[deque[0]] < K):
                while deque and running[r] <= running[deque[-1]]:
                    deque.pop()
                deque.append(r)
                r += 1
            if r == len(running):
                break
            while deque and running[r] - running[deque[0]] >= K:
                l = deque.popleft()
                result = min(result, r - l)
        return result if result != math.inf else -1
        '\n        \n                    #pop the last of the queue if it is smaller to maintain mono increasing queue \n                while deque and running[r] <= running[deque[-1]]: \n                    deque.pop()\n                    \n                    \n        l = 0\n        r = 1 \n        \n        while r < len(running): \n            \n            while r < len(running) and running[r] - running[l] < K: \n                r += 1 \n            while l < r and running[r] - running[l+1] >= K: \n                l += 1\n            result = min(result, r-l)\n            r += 1\n            l  += 1\n            \n        return result\n            \n        \n            while r < len(running): \n            while deque and running[r] - running[deque[0]] >= K:\n                result = min(result, i-deque[0])\n                deque.popleft()\n            while deque and running[r] <= running[deque[-1]]:\n                deque.pop()\n            deque.append(r)\n            \n        return result if result != math.inf else -1\n    \n    \n                \n            while r < len(running)-1 and running[r] - running[l] < s: \n                r += 1 \n\n            while l < r and running[r] - running[l] >= s:\n                result = min(result, r-l)                \n                l += 1\n                \n            r += 1\n        '
