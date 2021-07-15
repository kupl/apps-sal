t = int(input())
for i in range(t):
    a, b, c, r = list(map(int, input().split()))

    s = max(min(a, b), c - r)
    f = min(max(a, b), c + r)

    l = max(0, f - s)
    print(abs(a - b) - l)

