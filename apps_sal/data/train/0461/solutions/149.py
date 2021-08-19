class Node:

    def __init__(self, id, informTime=0):
        self.id = id
        self.employees = []
        self.informTime = informTime


class Solution:

    def construct_tree(self, headID, managers, informTime):
        manager_to_employees = {}
        for (employee, manager) in enumerate(managers):
            if manager in manager_to_employees:
                manager_to_employees[manager].append(employee)
            else:
                manager_to_employees[manager] = [employee]
        root = Node(headID, informTime[headID])
        stack = [root]
        while stack:
            node = stack.pop()
            if node.id not in manager_to_employees:
                continue
            for employee in manager_to_employees[node.id]:
                next_node = Node(employee, informTime[employee])
                node.employees.append(next_node)
                stack.append(next_node)
        return root

    def shortest_informTime(self, root):
        max_time = 0
        if root and root.employees:
            for employee in root.employees:
                max_time = max(max_time, self.shortest_informTime(employee))
            max_time += root.informTime
        return max_time

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        root = self.construct_tree(headID, manager, informTime)
        return self.shortest_informTime(root)
