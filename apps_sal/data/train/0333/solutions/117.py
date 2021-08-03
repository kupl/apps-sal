from collections import deque
from collections import defaultdict


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        d = defaultdict(list)
        for i, num in enumerate(arr):
            d[num].append(i)
        length = len(arr)
        q = deque()
        level = 0
        q.append(0)
        s = set()
        s.add(0)
        while(len(q) > 0):
            size = len(q)
            while size > 0:
                top = q.popleft()
                # if top == length - 1:
                #     return level
                if top - 1 >= 0 and top - 1 not in s:
                    s.add(top - 1)
                    q.append(top - 1)
                if top + 1 < length and top + 1 not in s:
                    if top + 1 == length - 1:
                        return level + 1
                    s.add(top + 1)
                    q.append(top + 1)
                for i in range(len(d[arr[top]])):
                    idx = d[arr[top]][len(d[arr[top]]) - 1 - i]
                    if idx not in s:
                        if idx == length - 1:
                            return level + 1
                        q.append(idx)
                        s.add(idx)
                size -= 1
            level += 1
        return level
