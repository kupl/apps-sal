from collections import deque
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        maxFruits = 0
        fruitTypes = set()        
        queue = deque()
        
        for i in tree:
            if i in fruitTypes or len(fruitTypes) < 2:
                fruitTypes.add(i)
            else:
                prevFruit = queue[-1]
                j = len(queue)-2
                while j >= 0 and queue[j] == prevFruit:
                    j -= 1
                while j >=0:
                    queue.popleft()
                    j -= 1
                for k in list(fruitTypes):
                    if k == prevFruit:
                        continue
                    else:
                        fruitTypes.remove(k)
                fruitTypes.add(i)
            queue.append(i)
            maxFruits = max(len(queue), maxFruits)
        return maxFruits
            
            

