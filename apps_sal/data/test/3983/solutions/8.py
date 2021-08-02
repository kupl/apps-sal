import sys
input = sys.stdin.readline

T = int(input())
for tests in range(T):
    N, M = map(int, input().split())
    E = [[] for i in range(N + 1)]

    for i in range(M):
        x, y = map(int, input().split())
        E[x].append(y)
        E[y].append(x)

    if N % 2 == 1:
        if (N * (N - 1) // 2 - M) % 2 == 1:
            print("First")
        else:
            print("Second")
        continue

    Q = [1]
    USE = [0] * (N + 1)
    USE[1] = 1
    sc1 = 1
    while Q:
        x = Q.pop()
        for to in E[x]:
            if USE[to] == 0:
                Q.append(to)
                sc1 += 1
                USE[to] = 1

    Q = [N]
    USE = [0] * (N + 1)
    USE[N] = 1
    sc2 = 1
    while Q:
        x = Q.pop()
        for to in E[x]:
            if USE[to] == 0:
                Q.append(to)
                sc2 += 1
                USE[to] = 1

    if sc1 % 2 != sc2 % 2:
        print("First")
    else:
        if sc1 % 2 == 0:
            if (N * (N - 1) // 2 - M) % 2 == 0:
                print("Second")
            else:
                print("First")
        else:
            if (N * (N - 1) // 2 - M) % 2 == 0:
                print("First")
            else:
                print("Second")
