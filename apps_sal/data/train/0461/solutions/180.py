class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        max_time = 0
        node_stack = []
        for node in manager:
            time = 0
            while node != -1:
                node_stack.append(node)
                node = manager[node]
            while node_stack:
                node = node_stack.pop()
                time += informTime[node]
                informTime[node] = time
                manager[node] = -1
                if time > max_time:
                    max_time = time
        return max_time
