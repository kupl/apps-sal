class Solution:

    def racecar1(self, target: int) -> int:
        q = collections.deque()
        q.append([0, 1])
        visited = set()
        visited.add('0_1')
        visited.add('0_-1')
        steps = 0
        while q:
            qsize = len(q)
            for i in range(qsize):
                (pos, speed) = q.popleft()
                pos1 = pos + speed
                speed1 = speed * 2
                if pos1 == target:
                    return steps + 1
                p1 = [pos1, speed1]
                if abs(speed1) < 2 * target and abs(pos1) < 2 * target and (not key1 in visited):
                    q.append(p1)
                speed2 = -1 if speed > 0 else 1
                p2 = [pos, speed2]
                key2 = '{}_{}'.format(pos, speed2)
                if key2 not in visited:
                    q.append(p2)
                    visited.add(key2)
            steps += 1
        return -1

    def racecar(self, target):
        k = target.bit_length() + 1
        barrier = 1 << k
        pq = [(0, target)]
        dist = [float('inf')] * (2 * barrier + 1)
        dist[target] = 0
        while pq:
            (steps, targ) = heapq.heappop(pq)
            if dist[targ] > steps:
                continue
            for k2 in range(k + 1):
                walk = (1 << k2) - 1
                (steps2, targ2) = (steps + k2 + 1, walk - targ)
                if walk == targ:
                    steps2 -= 1
                if abs(targ2) <= barrier and steps2 < dist[targ2]:
                    heapq.heappush(pq, (steps2, targ2))
                    dist[targ2] = steps2
        return dist[0]
