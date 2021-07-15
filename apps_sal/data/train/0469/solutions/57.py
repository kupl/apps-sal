class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # all nodes shoud not have more than 1 in degrees
        indegrees = [0]*n
        root = -1
        for i in range(n):
            left = leftChild[i]
            if left != -1:
                indegrees[left] += 1
                if indegrees[left] > 1:
                    return False
                
            right = rightChild[i]
            if right != -1:
                indegrees[right] += 1
                if indegrees[right] > 1:
                    return False
        
        # find the root with indegree == 0
        # if no root or multiple roots exist, return False
        for i in range(n):
            if indegrees[i] == 0:
                if root == -1:
                    root = i
                else:
                    return False
                
        if root == -1:
            return False
        
        # start from root, check node count == n
        def count(node):
            if node == -1:
                return 0
            return 1 + count(leftChild[node]) + count(rightChild[node])
        
        return count(root) == n

