class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        bus2bus = defaultdict(set)
        stop2bus = defaultdict(set)
        dq = deque()
        seen = set()
        dest = set()
        cnt = 1

        for i, route in enumerate(routes):
            for s in route:
                for b in stop2bus[s]:
                    bus2bus[i].add(b)
                    bus2bus[b].add(i)

                stop2bus[s].add(i)
                if s == S:
                    seen.add(i)
                if s == T:
                    dest.add(i)
        dq.extend(seen)
        while dq:
            length = len(dq)

            for _ in range(length):
                curr = dq.popleft()

                if curr in dest:
                    return cnt

                for nxt in bus2bus[curr]:
                    if nxt in seen:
                        continue

                    seen.add(nxt)
                    dq.append(nxt)

            cnt += 1

        return -1
