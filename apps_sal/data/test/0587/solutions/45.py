import sys
from operator import itemgetter
from heapq import *
input = sys.stdin.readline


def main():
    (n, k) = list(map(int, input().split()))
    sushi = [list(map(int, input().split())) for _ in range(n)]
    sushi.sort(key=itemgetter(1), reverse=True)
    key = []
    already = [False] * (n + 1)
    variety = k
    taste = 0
    for i in range(k):
        (v, t) = sushi[i]
        taste += t
        if already[v]:
            variety -= 1
            heappush(key, t)
            continue
        already[v] = True
    ans = [variety ** 2 + taste]
    for i in range(k, n):
        if variety == k:
            break
        (v, t) = sushi[i]
        if already[v]:
            continue
        already[v] = True
        taste += t - key[0]
        heappop(key)
        variety += 1
        ans.append(variety ** 2 + taste)
    print(max(ans))


def __starting_point():
    main()


__starting_point()
