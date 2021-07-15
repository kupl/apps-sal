from collections import deque


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        class TreeNode():
            def __init__(self, time=0):
                self.children = []
                self.time = time

        tree_nodes = [None for _ in range(n)]
        for index in range(n):
            # Set up child
            if tree_nodes[index] is None:
                tree_nodes[index] = TreeNode(time=informTime[index])
                
            # Set up parent
            if manager[index] != -1:
                if tree_nodes[manager[index]] is None:
                    tree_nodes[manager[index]] = TreeNode(time=informTime[manager[index]])

                tree_nodes[manager[index]].children.append(index)
                
            
        def BFS(root: TreeNode) -> int:
            longest_time = 0
            queue = deque()
            queue.append(root)
            
            while len(queue):
                node = queue.popleft()
                
                longest_time = max(longest_time, node.time)
                
                for child in node.children:
                    tree_nodes[child].time += node.time
                    queue.append(tree_nodes[child])
                    
            return longest_time
        
        return BFS(tree_nodes[headID])
            
        ##############################
        
        def sum_leaf_to_root(leaf: int) -> int:
            if leaf == headID:
                return informTime[headID]
            
            boss = manager[leaf]
            total_time = 0
            
            while boss != headID:
                total_time += informTime[boss]
                boss = manager[boss]
                
            total_time += informTime[headID]
            
            return total_time
        
        return max(
            sum_leaf_to_root(leaf)
            for leaf in (
                index
                for index in range(len(manager))
                if index not in manager
            )
        )
