t = int(input())

for i in range(t):
    n, x, m = map(int, input().split())
    leftMost = x
    rightMost = x
    for j in range(m):
        l, r = map(int, input().split())
        if l > rightMost:
            continue
        if r < leftMost:
            continue
        leftMost = min(l, leftMost)
        rightMost = max(r, rightMost)
    print(rightMost - leftMost + 1)
