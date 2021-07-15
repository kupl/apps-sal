class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        ans = 0
        n = len(routes)
        if S == T:
            return 0
        graph = collections.defaultdict(set)# stop -> bus #
        queue = collections.deque()
        visited_stop = set()
        visited_bus = set()
        for i in range(n):
            for stop in routes[i]:
                graph[stop].add(i)
        print(graph)
        queue.append(S)
        visited_stop.add(S)
        
        while queue:
            qLen = len(queue)
            ans +=1
            for i in range(qLen):
                stop = queue.popleft()
                for next_bus in graph[stop]:
                    if next_bus in visited_bus:
                        continue
                    visited_bus.add(next_bus)
                    for next_stop in routes[next_bus]:
                        if next_stop in visited_stop:
                            continue
                        if next_stop == T:
                            print('here')
                            return ans
                        queue.append(next_stop)
                        visited_stop.add(next_stop)
            # print(queue, visited_stop, visited_bus)
            
            # print(ans)
        return -1 
    
# defaultdict(<class 'set'>, {1: {0}, 2: {0}, 7: {0, 1}, 3: {1}, 6: {1}})
# deque([2]) {1, 2} {0}
# deque([2, 7]) {1, 2, 7} {0}
# 1
# deque([3]) {1, 2, 3, 7} {0, 1}
            

           

