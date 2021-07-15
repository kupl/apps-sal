class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        n = len(status)
        
        self.count = 0
        
        queue = collections.deque([i for i in initialBoxes if status[i]==1])
        
        for i in queue:
            status[i] = 2
        
        boxSet = set(initialBoxes)
        keySet = set(i for i in range(n) if status[i]==1)
        
        while (queue):
            l = len(queue)
            for i in range(l):
                cur = queue.popleft()
                self.count += candies[cur]
                for box in containedBoxes[cur]:
                    boxSet.add(box)
                    if box in keySet and status[box] != 2:
                        queue.append(box)
                        status[box] = 2
                        print(box)
                for key in keys[cur]:
                    keySet.add(key)
                    if key in boxSet and status[key] != 2:
                        queue.append(key)
                        status[key] = 2
                        print(key)

                    
        
        return self.count

