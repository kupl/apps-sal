from heapq import heappop, heappush, heapify


class RemovableHeap(list):
    from heapq import heappop, heappush, heapify

    def __init__(self, *args, **kwargs):
        self.unremoved_elements = []

    def remove(self, value):
        heappush(self.unremoved_elements, value)
        while self.unremoved_elements and self.unremoved_elements[0] == self[0]:
            heappop(self.unremoved_elements)
            heappop(self)


(N, Q) = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(Q)]
M = 2 * 10 ** 5
maxA = 10 ** 9
for i in range(N):
    AB[i][1] -= 1
for i in range(Q):
    CD[i][0] -= 1
    CD[i][1] -= 1
youchiens = [RemovableHeap() for _ in range(M)]
for (a, b) in AB:
    youchiens[b].append(-a)
for i in range(Q):
    heapify(youchiens[i])
saikyoenjis = RemovableHeap()
for youchien in youchiens:
    if youchien:
        saikyoenjis.append(-youchien[0])
heapify(saikyoenjis)
ans = []
for (c, d) in CD:
    old_youchien = AB[c][1]
    saikyoenjis.remove(-youchiens[old_youchien][0])
    youchiens[old_youchien].remove(-AB[c][0])
    if youchiens[old_youchien]:
        heappush(saikyoenjis, -youchiens[old_youchien][0])
    if youchiens[d]:
        saikyoenjis.remove(-youchiens[d][0])
    heappush(youchiens[d], -AB[c][0])
    heappush(saikyoenjis, -youchiens[d][0])
    ans.append(saikyoenjis[0])
    AB[c][1] = d
print(*ans, sep='\n')
