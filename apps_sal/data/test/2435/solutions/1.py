t = int(input())
for _ in range(t):
    (n, x, m) = map(int, input().split())
    l = x
    r = x
    for i in range(m):
        (a, b) = map(int, input().split())
        if r >= a and l <= b:
            l = min(l, a)
            r = max(r, b)
    print(r - l + 1)
