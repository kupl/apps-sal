class Node:
    
    def __init__(self, unique_id, information_time):
        self.information_time = information_time
        self.unique_id = unique_id
        self.childrens = []
        
    def add_child(self, child):
        self.childrens.append(child)

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        root = Node(headID, informTime[headID]) # 0
        id_node_mapping = {headID: root} # {0: (0, 0)}
        
        def dfs(node):
            max_time = 0
            for child in node.childrens:
                max_time = max(dfs(child), max_time)
                
            return max_time + node.information_time
        
        for i, (parent, timetaken) in enumerate(zip(manager, informTime)):
            
            if i not in id_node_mapping:
                id_node_mapping[i] = Node(i, timetaken)
            else:
                id_node_mapping[i].information_time = timetaken
                
            if parent not in id_node_mapping:
                id_node_mapping[parent] = Node(parent, 0)
                
            id_node_mapping[parent].add_child(id_node_mapping[i])
            
        return dfs(root)

