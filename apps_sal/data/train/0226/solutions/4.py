class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        ''' 
        # graph of indices, works if we don't have duplicate elements
        graph = collections.defaultdict(list)
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if int((A[i]+A[j])**0.5)**2==(A[i]+A[j]):
                    graph[i] += [j]
                    graph[j] += [i]
        # source node
        graph[-1] = [i for i in range(len(A))]
        def dfs(node, visited):
            if len(visited)==len(A):
                return 1
            res = 0
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                res += dfs(neighbor, visited|{neighbor})
            return res
        return dfs(-1, set())
        '''
        candidates = collections.Counter(A)
        graph = {x: [y for y in candidates if int((x + y)**0.5)**2 == x + y] for x in candidates}
        # source node
        graph[-1] = [x for x in candidates]

        def dfs(node, node_left):
            if node_left == 0:
                return 1
            res = 0
            for n in graph[node]:
                if candidates[n] == 0:
                    continue
                candidates[n] -= 1
                res += dfs(n, node_left - 1)
                candidates[n] += 1
            return res
        return dfs(-1, len(A))
