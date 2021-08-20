t = int(input())
for _ in range(t):
    (a, b, c, r) = list(map(int, input().strip().split()))
    (a, b) = (min(a, b), max(a, b))
    low = max(a, c - r)
    high = min(b, c + r)
    unavaialbe = high - low
    unavaialbe = max(unavaialbe, 0)
    print(b - a - unavaialbe)
