import copy
from collections import deque


def BFS(N, M, List):
    Edge = [[] for TN in range(N + 1)]
    for TM in range(0, M):
        Edge[List[TM][0]].append(List[TM][1])
        Edge[List[TM][1]].append(List[TM][0])

    Distance = [-1] * (N + 1)
    Distance[0] = 0
    Distance[1] = 0

    From = [0] * (N + 1)
    From[1] = 1

    Deque = deque()
    Deque.append(1)
    while Deque:
        Now = Deque.popleft()
        for Con in Edge[Now]:
            if Distance[Con] == -1:
                Distance[Con] = Distance[Now] + 1
                Deque.append(Con)
                From[Con] = Now

    return Distance[1:], From[1:]


N, M = (int(T) for T in input().split())
List = [[] for TM in range(0, M)]
for TM in range(0, M):
    List[TM] = [int(T) for T in input().split()]
Count = 0
for TM in range(0, M):
    ListCopy = copy.deepcopy(List)
    del ListCopy[TM]
    Distance, From = BFS(N, M - 1, ListCopy)
    if -1 in Distance:
        Count += 1
print(Count)
