class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        tree = {}
        for i in range(len(manager)):
            if manager[i] in tree:
                tree[manager[i]].append(i)
            else:
                tree[manager[i]] = [i]

        queue = [(headID, informTime[headID])]
        solution = -1
        while queue:
            node, time = queue.pop(0)
            solution = max(solution, time)

            if node in tree:
                for n in tree[node]:
                    queue.append((n, time + informTime[n]))

        return solution
