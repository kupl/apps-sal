class Node:
    def __init__(self, val, weight=0):
        self.root = val
        self.weight = weight
        self.children = []


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        hashmap = {}

        for i in range(n):
            hashmap.update({i: Node(i)})

        for i, item in enumerate(manager):
            if item == -1:
                head = hashmap[i]
            else:
                hashmap[item].children.append(hashmap[i])

        for i, time in enumerate(informTime):
            hashmap[i].weight = time

        def recur(root) -> int:
            if not root.children:
                return root.weight

            max_time = 0
            for child in root.children:
                time = recur(child)
                if time > max_time:
                    max_time = time

            return root.weight + max_time

        return recur(head)
