class Employee:
    def __init__(self, idx, inf_time):
        self.idx = idx
        self.inf_time = inf_time
        self.subs = []

class Solution:            
    def numOfMinutesCoool(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(i):
            if manager[i] != -1:
                informTime[i] += dfs(manager[i])
                manager[i] = -1
            return informTime[i]
        return max(map(dfs, manager))
    
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subs_dct = defaultdict(list)
        for empl, manager in enumerate(manager):
            subs_dct[manager].append(empl)
        
        root = Employee(headID, informTime[headID])
        def makeTree(node):
            for sub in subs_dct[node.idx]:
                node.subs.append(Employee(
                    sub,
                    node.inf_time + informTime[sub]
                ))
            for sub_node in node.subs:
                makeTree(sub_node)
        makeTree(root)
        
        total = 0
        def dfs(node):
            if not node.subs:
                return node.inf_time
            return max([dfs(sub_node) for sub_node in node.subs])
        
        return dfs(root)
