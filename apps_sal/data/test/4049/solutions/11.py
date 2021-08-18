import sys
input = sys.stdin.readline

n = int(input())
a1, a2, a3 = list(map(int, input().split()))
b1, b2, b3 = list(map(int, input().split()))

V = 8

EDGE = [[0] * V for i in range(V)]

start = 0
goal = V - 1

EDGE[0][1] = a1
EDGE[0][2] = a2
EDGE[0][3] = a3

EDGE[4][7] = b1
EDGE[5][7] = b2
EDGE[6][7] = b3

EDGE[1][4] = float("inf")
EDGE[1][6] = float("inf")

EDGE[2][4] = float("inf")
EDGE[2][5] = float("inf")

EDGE[3][5] = float("inf")
EDGE[3][6] = float("inf")

ANS = 0
while True:
    USED = [0] * V
    ROUTE = [-1] * V
    Q = [(start, float("inf"))]

    while Q:
        NOW, cost = Q.pop()
        if NOW == goal:
            break

        for to in range(V):
            if USED[to] == 0 and EDGE[NOW][to] != 0:
                ROUTE[to] = NOW
                USED[to] = 1
                Q.append((to, min(cost, EDGE[NOW][to])))
    else:
        break

    ANS += cost
    i = goal
    while i != start:
        j = ROUTE[i]
        EDGE[j][i] -= cost
        EDGE[i][j] += cost
        i = j

print(n - ANS, min(a1, b2) + min(a2, b3) + min(a3, b1))
