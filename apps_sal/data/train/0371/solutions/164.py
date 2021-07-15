class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S==T: return 0
        map = defaultdict(list)
        starting_buses = []
        for bus, route in enumerate(routes):   
          for stop in route:
            if stop == S: starting_buses.append(bus)
            map[stop].append(bus)
    
        visited_stops = set()
        q = deque()
        min_buses = float('inf')
        for starting_bus in starting_buses:
          q.append((starting_bus,1))
          visited_stops.add(S)
  
        while q:
            bus, num_bus = q.pop()
            if num_bus == min_buses: continue
            for stop in routes[bus]:
              if stop == T:
                min_buses = min(min_buses, num_bus)
                break
              if stop not in visited_stops:
                visited_stops.add(stop)
                for next_bus in map[stop]:
                  if next_bus == bus: continue
                  q.append((next_bus, num_bus+1))
          
        return min_buses if min_buses != float('inf') else -1

