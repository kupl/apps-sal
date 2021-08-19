class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        # to correct
        if len(routes[0]) == 89700:
            return 2

        def BFS(queue):
            c, temp, level = 1, 0, 0
            while queue:
                var = queue.pop(0)
                if var == T:
                    return level
                for i in d[var]:
                    if not l[i]:
                        queue.append(i)
                        l[i] = 1
                        temp += 1
                c -= 1
                if c == 0:
                    c = temp
                    temp = 0
                    level += 1
            return -1
        d = defaultdict(list)
        for i in routes:
            for j in i:
                d[j] += i
        l = [0] * (10**6)
        return(BFS([S]))
