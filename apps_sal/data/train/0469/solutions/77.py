from collections import deque


class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        q = deque()
        visited = [0 for _ in range(len(leftChild))]
        root = 0
        store = set([i for i in range(len(leftChild))])
        for i in range(len(leftChild)):
            left = leftChild[i]
            right = rightChild[i]
            store.discard(left)
            store.discard(right)
        print(store)
        for i in store:
            root = i
            break
        q.append(root)
        while len(q) > 0:
            element = q.popleft()
            visited[element] = 1
            left = leftChild[element]
            right = rightChild[element]
            if left != -1:
                if left in q or visited[left] == 1:
                    return False
                else:
                    q.append(left)
            if right != -1:
                if right in q or visited[right] == 1:
                    return False
                else:
                    q.append(right)
        for i in visited:
            if i == 0:
                return False
        return True
