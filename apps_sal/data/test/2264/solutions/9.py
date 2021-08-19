t = int(input())
for i in range(t):
    n = int(input())
    r = 10 ** 9 + 1
    l = 0
    for i in range(n):
        (x, y) = map(int, input().split())
        r = min(r, y)
        l = max(x, l)
    print(max(0, l - r))
