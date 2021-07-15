from collections import defaultdict
from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        '''
        node1 => {1,2,7}
        1 => node1
        3 => node2
        2 => node1
        6 => node2
        7 => node1, node2
        
        node2 => {3,6,7}
        '''
        buses = defaultdict(list) ## map stops to buses
        for i in range(len(routes)):
            for stop in routes[i]:
                buses[stop].append(i)
                
        queue = deque([(S,0)])
        busVisited = set()
        while queue:
            stop, busCnt = queue.popleft()
            if stop == T:
                return busCnt
            for bus in buses[stop]:
                if bus in busVisited:
                    continue
                busVisited.add(bus)
                for reachableStop in routes[bus]:
                    #if reachableStop not in visited:
                    queue.append((reachableStop, busCnt+1))
            
        return -1   
            

