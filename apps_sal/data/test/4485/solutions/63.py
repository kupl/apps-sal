import typing
from typing import Deque, Set, Dict


class Island:
    def __init__(self, id: int) -> None:
        self.id: int = id
        self.connection: List['Island'] = []
        self.rank: int = 0

    def addConnection(self, other: 'Island') -> None:
        self.connection.append(other)
        other.connection.append(self)

    def setRank(self, other: 'Island') -> None:
        self.rank = other.rank + 1


class Islands(Dict[int, Island]):
    def __init__(self, num: int):
        for id in range(1, num + 1):
            self[id] = Island(id)


def bfs(root: Island, max_depth: int) -> None:
    reserved: Deque[Island] = Deque([root])
    seen: Set[int] = {root.id}
    while len(reserved) != 0:
        current: Island = reserved.popleft()
        if current.rank > max_depth:
            break
        for connected in current.connection:
            if connected.id in seen:
                continue
            connected.setRank(current)
            seen.add(connected.id)
            reserved.append(connected)


def main() -> None:
    with open(0) as f:
        N, M = map(int, f.readline().split())
        ab = [map(int, line.split()) for line in f.readlines()]
    # 諸島生成
    islands: Islands = Islands(N)
    # 諸島間定期便生成
    for a, b in ab:
        islands[a].addConnection(islands[b])
    # bfs
    bfs(islands[1], 2)
    # 出力
    print('POSSIBLE' if islands[N].rank in (1, 2) else 'IMPOSSIBLE')


def __starting_point():
    main()


__starting_point()
