from heapq import *
n = int(input())
a = list(map(int, input().split()))
s = 0
if len(a) % 2 == 0:
    a = [0] + a
    n += 1


def sc(a, s=0):
    heapify(a)
    for i in range((n - 1) // 2):
        k = heappop(a) + heappop(a) + heappop(a)
        s += k
        heappush(a, k)
    print(s)


sc(a)
