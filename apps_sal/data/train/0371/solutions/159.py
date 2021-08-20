class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        n = len(routes)
        for i in range(n):
            routes[i].sort()
        graph = [[] for i in range(n)]
        for i in range(n):
            for j in range(i):
                if self.haveCommonValues(routes[i], routes[j]):
                    graph[i].append(j)
                    graph[j].append(i)
        print(graph)
        targets = set()
        vis = set()
        for i in range(n):
            if self.binary_search(routes[i], T):
                targets.add(i)
            if self.binary_search(routes[i], S):
                vis.add(i)
        print(vis)
        print(targets)
        step = 1
        q = list(vis)
        while q:
            temp = []
            for cur in q:
                if cur in targets:
                    return step
                for nei in graph[cur]:
                    if nei not in vis:
                        vis.add(nei)
                        temp.append(nei)
            q = temp
            step += 1
        return -1

    def binary_search(self, A, target):
        l = 0
        r = len(A) - 1
        while l <= r:
            mid = (l + r) // 2
            if A[mid] == target:
                return True
            if target < A[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False

    def haveCommonValues(self, A, B):
        i = 0
        j = 0
        while i < len(A):
            while j < len(B) and B[j] < A[i]:
                j += 1
            if j == len(B):
                return False
            if B[j] == A[i]:
                return True
            i += 1
        return False
