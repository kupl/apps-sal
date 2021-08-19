class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        V = numCourses

        # Store outgoing edges
        edges = []

        for _ in range(V):
            edges.append(set())

        for p in prerequisites:
            # Edge goes from v1 to v2
            v2, v1 = p
            edges[v1].add(v2)

        checked = set()

        def detect_cycle(x, visited):
            visited.add(x)
            checked.add(x)

            for v in edges[x]:
                if v in visited:
                    return True
                if detect_cycle(v, visited):
                    return True
            visited.remove(x)
            return False

        for v in range(V):
            if v in checked:
                continue
            if detect_cycle(v, set()):
                return False

        return True
