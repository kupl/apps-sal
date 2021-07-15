class Node:
    def __init__(self,id,time):
        self.id = id
        self.informTime = time
        self.children = set()
        
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        nodes = [Node(x,informTime[x]) for x in range(n)]
        for i,v in enumerate(manager):
            if v == -1:continue
            nodes[v].children.add(nodes[i])        
            
        def recursive(node):
            if not node:return 0
            temp = 0
            for n in node.children:
                temp = max(temp,recursive(n))
            return temp+node.informTime
        
        return recursive(nodes[headID])
            

