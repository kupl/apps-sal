def createGraph(manager: List[int]):
    graph = collections.defaultdict(set)
    for i, employee in enumerate(manager):
        graph[employee].add(i)
    return graph

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = createGraph(manager)
        stack = [(0, headID)]
        visited = set()
        while stack:
            depth, employeeId = stack.pop()
            if employeeId not in visited:
                visited.add(employeeId)
                if manager[employeeId] != -1:
                    informTime[employeeId] += informTime[manager[employeeId]]
                for employee in graph[employeeId]:
                    stack.append((depth+1, employee))
        return max(informTime)
