class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        visited = [0 for _ in range(n)]
        from collections import deque
        for i in range(n):
            if visited[i] == 1:
                continue
            q = deque()
            q.append(i)
            visited[i] = 1
            while q:
                cur = q.popleft()
                left = leftChild[cur]
                right = rightChild[cur]
                if left != -1:
                    if visited[left] == 1:
                        return False
                    else:
                        visited[left] = 1
                        q.append(left)
                if right != -1:
                    if visited[right] == 1:
                        return False
                    else:
                        visited[right] = 1
                        q.append(right)
            visited[i] = 0
            leftChild[i] = -1
            rightChild[i] = -1
        return n - sum(visited) == 1
