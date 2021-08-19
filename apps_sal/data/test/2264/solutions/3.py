t = int(input())
INF = 10000000000.0
for i in range(t):
    n = int(input())
    mini = INF
    maxi = -INF
    for i in range(n):
        (a, b) = map(int, input().split())
        maxi = max(a, maxi)
        mini = min(b, mini)
    print(max(maxi - mini, 0))
