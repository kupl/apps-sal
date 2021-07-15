class Solution:
    def minDays(self, n: int) -> int:
        queue = collections.deque()
        
        queue.append(n)
        level = 0
        seen = set()
        while queue:
            subList = set()
            for i in range(len(queue)):
                oranges = queue.popleft()
                if oranges not in seen:
                    subList.add(oranges-1)
                    if oranges%2 == 0:
                        subList.add(oranges - (oranges//2))
                    if oranges%3 == 0:
                        subList.add(oranges - (2*(oranges//3)))
            
            level += 1
            if 0 in subList:
                return level
            for val in subList:
                queue.append(val)
            

