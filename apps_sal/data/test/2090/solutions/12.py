from collections import defaultdict as dd
import math
import heapq


def nn():
    return int(input())


def li():
    return list(input())


def mi():
    return list(map(int, input().split()))


def lm():
    return list(map(int, input().split()))


(n, k) = mi()
songs = []
for i in range(n):
    songs.append(lm())
songs.sort(key=lambda x: -x[1])
h = []
maxsofar = 0
newlen = 0
for i in range(k):
    beauty = songs[i][1]
    h.append(songs[i][0])
    newlen += songs[i][0]
    maxsofar = max(maxsofar, newlen * beauty)
heapq.heapify(h)
for i in range(k, n):
    if songs[i][0] > h[0]:
        beauty = songs[i][1]
        removed = heapq.heappushpop(h, songs[i][0])
        newlen += songs[i][0] - removed
        maxsofar = max(maxsofar, newlen * beauty)
print(maxsofar)
