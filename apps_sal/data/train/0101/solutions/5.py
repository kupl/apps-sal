t = int(input())
for i in range(t):
    a, b, c, r = list(map(int, input().split()))
    if b < a:
        a, b = b, a
    k = min(c + r, b) - max(c - r, a)
    d = b - a
    if k <= 0:
        print(d)
    else:
        print(d - k)
