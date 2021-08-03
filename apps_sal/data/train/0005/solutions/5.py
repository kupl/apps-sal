from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    liste = list(map(int, input().split()))
    vis = [0 for i in range(n)]
    can = [0 for i in range(n)]
    can2 = [0 for i in range(n)]
    maxi = 0
    for i in range(1, n):
        if (vis[liste[i - 1]]):
            break
        vis[liste[i - 1]] = 1
        maxi = max(maxi, liste[i - 1])
        if (maxi == i):
            can[maxi] = 1
    liste = liste[::-1]
    maxi = 0
    vis = [0 for i in range(n)]
    for i in range(1, n):
        if (vis[liste[i - 1]]):
            break
        vis[liste[i - 1]] = 1
        maxi = max(maxi, liste[i - 1])
        if (maxi == i):
            can2[maxi] = 1
    count = 0
    for i in range(1, n):
        if (can[i] and can2[n - i]):
            count += 1
    print(count)
    for i in range(1, n):
        if (can[i] and can2[n - i]):
            print(i, n - i)
