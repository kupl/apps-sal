import sys
from collections import deque
readline = sys.stdin.readline


def ns():
    return readline().rstrip()


def ni():
    return int(readline().rstrip())


def nm():
    return map(int, readline().split())


def nl():
    return list(map(int, readline().split()))


def solve():
    k = ni()
    q = deque()
    q.append(1)
    dist = [k] * k
    dist[1] = 1
    while q:
        v = q.popleft()
        if dist[(v + 1) % k] > dist[v] + 1:
            dist[(v + 1) % k] = dist[v] + 1
            q.append((v + 1) % k)
        if dist[v * 10 % k] > dist[v]:
            dist[v * 10 % k] = dist[v]
            q.appendleft(v * 10 % k)
    print(dist[0])
    return


solve()
