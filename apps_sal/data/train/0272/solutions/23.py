class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        visited = [0] * n
        unopened = [0] * n
        opened = []
        
        ans = 0
        for b in initialBoxes:
            if status[b] == 1:
                opened.append(b)
                visited[b] = 1
            else:
                unopened[b] = 1
        while opened:
            q2 = []
            for b in opened:
                ans += candies[b]
                for bb in containedBoxes[b]:
                    if visited[bb] == 0:
                        if status[bb] == 1:
                            q2.append(bb)
                        else:
                            unopened[bb] = 1
                for k in keys[b]:
                    status[k] = 1
                    if unopened[k] == 1 and visited[k] == 0:
                        unopened[k] = 0
                        visited[k] = 1
                        q2.append(k)
            opened = q2
        return ans
    
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        visited = [0] * n
        unopened = [0] * n
        opened = collections.deque()
        
        ans = 0
        for b in initialBoxes:
            if status[b] == 1:
                opened.append(b)
                visited[b] = 1
            else:
                unopened[b] = 1
        while opened:
            b = opened.popleft()
            ans += candies[b]
            for bb in containedBoxes[b]:
                if visited[bb] == 0:
                    if status[bb] == 1:
                        opened.append(bb)
                    else:
                        unopened[bb] = 1
            for k in keys[b]:
                status[k] = 1
                if unopened[k] == 1 and visited[k] == 0:
                    unopened[k] = 0
                    visited[k] = 1
                    opened.append(k)
        return ans
            

