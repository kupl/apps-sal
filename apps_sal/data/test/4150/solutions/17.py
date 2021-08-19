import heapq
(n, k) = map(int, input().split())
a = list(map(int, input().split()))
first = [False] * n
second = [False] * n
pq = []
nexts = [None] * n
prevs = [None] * n
for i in range(n):
    heapq.heappush(pq, (-a[i], i))
    if i < n - 1:
        nexts[i] = i + 1
    if i > 0:
        prevs[i] = i - 1
turn = 0
while pq:
    (_, curIdx) = heapq.heappop(pq)
    if first[curIdx] or second[curIdx]:
        continue
    if turn == 0:
        first[curIdx] = True
    else:
        second[curIdx] = True
    fromLeft = 0
    i = prevs[curIdx]
    while fromLeft < k and i != None:
        if turn == 0:
            first[i] = True
        else:
            second[i] = True
        i = prevs[i]
        fromLeft += 1
    prevs[curIdx] = i
    fromRight = 0
    i = nexts[curIdx]
    while fromRight < k and i != None:
        if turn == 0:
            first[i] = True
        else:
            second[i] = True
        i = nexts[i]
        fromRight += 1
    nexts[curIdx] = i
    if prevs[curIdx] != None:
        nexts[prevs[curIdx]] = nexts[curIdx]
    if nexts[curIdx] != None:
        prevs[nexts[curIdx]] = prevs[curIdx]
    turn ^= 1
for i in range(n):
    print(1 if first[i] else 2, end='')
