from heapq import *
n = int(input())
_a = list(map(int, input().split(" ")))
_t = list(map(int, input().split(" ")))
at = [[0, 0]]
for i in range(n):
    at.append([_a[i], _t[i]])
at.append([int(1e11), 0])
at.sort()


def __starting_point():
    Q = []
    s = 0
    cost = 0
    for i in range(1, n + 2):
        a = at[i - 1]
        b = at[i]
        num = a[0]
        while len(Q) > 0 and num < b[0]:
            s += heappop(Q)
            num += 1
            cost += s
        s += b[1]
        heappush(Q, -b[1])
        #print("{}, {}, {}".format(i, s, cost))
    print(cost)


__starting_point()
