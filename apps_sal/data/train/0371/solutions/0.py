from collections import defaultdict


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        # sequence_to_route_id dict
        # if when adding sequence ids to this dict, they are part of another route,
        # merge them
        max_int = 10**6
        start_routes = set()
        end_routes = set()
        route_connections = defaultdict(lambda: set())
        sequence_to_route_id_dict = {}
        route_to_minbuscount = defaultdict(lambda: max_int)
        for r_id, r in enumerate(routes):
            for s in r:
                if s == S:
                    start_routes.add(r_id)
                    route_to_minbuscount[r_id] = 1
                if s == T:
                    end_routes.add(r_id)
                if s in sequence_to_route_id_dict:
                    route_connections[r_id].add(sequence_to_route_id_dict[s])
                    route_connections[sequence_to_route_id_dict[s]].add(r_id)
                sequence_to_route_id_dict[s] = r_id

        # print(route_connections)
        # print(start_routes)
        # print(end_routes)

        current_route_buscount = [(s, 1) for s in start_routes]
        for r_id, buscount in current_route_buscount:
            # print(current_route_buscount)
            # print(dict(route_to_minbuscount))
            for connection in route_connections[r_id]:
                if route_to_minbuscount[connection] > buscount + 1:
                    route_to_minbuscount[connection] = buscount + 1
                    current_route_buscount.append((connection, buscount + 1))
        result = min(route_to_minbuscount[x] for x in end_routes)
        return -1 if result == max_int else result
