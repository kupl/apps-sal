import sys
from heapq import heapify, heappop, heappush
from collections import defaultdict


def sr():
    return sys.stdin.readline().rstrip()


def ir():
    return int(sr())


def lr():
    return list(map(int, sr().split()))


(N, Q) = lr()
top = []
left_top = []
infants = [[] for _ in range(2 * 10 ** 5 + 1)]
left = [[] for _ in range(2 * 10 ** 5 + 1)]
dic = defaultdict(list)
for i in range(1, N + 1):
    (a, b) = lr()
    heappush(infants[b], (-a, i))
    dic[i] = (a, b)
for i in range(1, 2 * 10 ** 5 + 1):
    if infants[i]:
        (rate, id) = infants[i][0]
        heappush(top, (-rate, id))
for _ in range(Q):
    (c, next) = lr()
    (r, prev) = dic[c]
    dic[c] = (r, next)
    (r3, prev_top) = infants[prev][0]
    heappush(left_top, (-r3, prev_top))
    heappush(left[prev], (-r, c))
    while infants[prev] and left[prev] and (infants[prev][0][1] == left[prev][0][1]):
        heappop(infants[prev])
        heappop(left[prev])
    if infants[prev]:
        (rate, id) = infants[prev][0]
        heappush(top, (-rate, id))
    if infants[next]:
        heappush(left_top, (-infants[next][0][0], infants[next][0][1]))
    heappush(infants[next], (-r, c))
    while left[next] and infants[next][0][1] == left[next][0][1]:
        heappop(infants[next])
        heappop(left[next])
    (r2, id2) = infants[next][0]
    heappush(top, (-r2, id2))
    while left_top and top[0][1] == left_top[0][1]:
        heappop(top)
        heappop(left_top)
    answer = top[0][0]
    print(answer)
