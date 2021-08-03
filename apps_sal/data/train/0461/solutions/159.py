from collections import deque


class Node:
    def __init__(self, id: int, inform_t: int):
        self.id = id
        self.children = []
        self.inform_t = inform_t

    def __repr__(self):
        return f'<{self.id} ({self.inform_t}): {len(self.children)}>'

    def total_inform_time(self):
        t = self.inform_t
        if self.children:
            t += max(ch.total_inform_time() for ch in self.children)
        return t


class Solution:

    def build_tree(self, manager: List[int], inform_time: List[int]) -> Node:
        nodes = [None] * len(manager)
        root = None
        for id, man_id in enumerate(manager):
            if nodes[id] is None:
                nodes[id] = Node(id, inform_time[id])

            if man_id >= 0:
                if nodes[man_id] is None:
                    nodes[man_id] = Node(man_id, inform_time[man_id])

                nodes[man_id].children.append(nodes[id])
            else:
                root = nodes[id]
        return root

    def numOfMinutes(self, n: int, head_id: int, manager: List[int], inform_time: List[int]) -> int:
        root = self.build_tree(manager, inform_time)
        return root.total_inform_time()
