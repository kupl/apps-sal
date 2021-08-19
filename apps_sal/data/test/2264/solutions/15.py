for i in range(int(input())):
    n = int(input())
    e = 10000000000000000
    s = -10000000000000000
    for i in range(n):
        (a, b) = map(int, input().split())
        e = min(e, b)
        s = max(a, s)
    print(max(0, s - e))
