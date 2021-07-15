t = int(input())
for i1 in range(t):
    n = int(input())
    a, b = (0, 10**9)
    for i in range(n):
        c, d = list(map(int, input().split()))
        b = min(d, b)
        a = max(a, c)
    print(max(0, a - b))

