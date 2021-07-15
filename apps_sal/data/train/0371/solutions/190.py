class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:

        md, que, visited, changes = collections.defaultdict(set), collections.deque(), set(), {}

        # prre-processing, we can get dict m[1] = (0), m[2] = (0), m[7] = (0,1) ,etc
        # means for stop 7 , bus 0, and 1 can reach
        for b, r in enumerate(routes):
            for s in r:
                md[s].add(b)

        # S or T not reachable
        if S not in md or T not in md:
            return -1

        # if S and T are same, we don't even need to take bus
        if S == T:
            return 0

        for b in md[S]:
            for stop in routes[b]:
                # (2,0,0), (7,0,0)
                # (1,0,0) - means stop 1, bus 0, bus changes 0
                que.append((stop, b, 1))
                # changes[1,0] = 0, changes[2,0] = 0, changes[7,0] = 0
                # means for reach 1,2,7 we just 1 times of bus change
                # (take the first bus also count as 1 change)
                changes[stop, b] = 1

        while que:
            stop, bus, times = que.popleft()
            # already reach the Target
            if stop == T:
                return times
            for b in md[stop]:
                if bus != b:
                    for stop in routes[b]:
                        # if I already reached this stop by bus, but I used few times for change
                        if (stop, bus) in changes and changes[stop, bus] > 1 + times:
                            que.append((stop, bus, 1 + times))
                            # remember update the new times in cache
                            changes[stop, bus] = 1 + times
                        elif (stop, bus) not in changes:  # I never reached stop by this bus yet
                            changes[stop, bus] = 1 + times
                            que.append((stop, bus, 1 + times))
                        # else: if I reached stop by bus, but I changed more times than the record in cache,
                        # just prunning it
                    # this sentences improve the performance greatly
                    # the time is from 5000ms decrease to 260 ms
                    routes[b] = []

        return -1


