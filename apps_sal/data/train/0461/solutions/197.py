class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # the employees are on a tree
        # each time we go down one level, we wait X minutes
        # the answer is the max among all leaf nodes (employees that don't manage)
        
        # first: creats aux data structures to support a tree-like interaction
        # given an employee: know it's children
        # build a map: key: employeeID -> List of children IDs
        
        # traverse the tree in BFS manner
        # once a leaf is found, update the solution
        
        tree = {}
        for i in range(len(manager)):
            if manager[i] in tree:
                tree[manager[i]].append(i)
            else:
                tree[manager[i]] = [i]
        
      
        queue = [(headID, informTime[headID])]
        solution = -1
        while queue:
            node, time = queue.pop(0)    
            solution = max(solution, time)
            
            if node in tree:
                for n in tree[node]:
                    queue.append((n, time + informTime[n]))
            
        
        return solution
