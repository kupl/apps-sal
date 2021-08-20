from heapq import heapify
from heapq import heappop


def cmp(a, b):
    return a[0] > a[1]


n = int(input())
arr = []
for i in range(n * 2):
    arr.append([None] * (n * 2))
elems = []
for i in range(1, n * 2):
    lst = list(map(int, input().split()))
    for j in range(len(lst)):
        elems.append([-lst[j], i, j])
heapify(elems)
players = [True] * (n * 2)
rez = [None] * (n * 2)
cnt = 0
while elems and cnt != n:
    (w, a, b) = heappop(elems)
    if players[a] and players[b]:
        players[a] = False
        players[b] = False
        cnt += 1
        rez[a] = b
        rez[b] = a
for i in range(n * 2):
    print(rez[i] + 1, end=' ')
