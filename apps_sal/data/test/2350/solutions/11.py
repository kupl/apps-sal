tt = int(input())
for loop in range(tt):
    (x1, y1, x2, y2) = list(map(int, input().split()))
    print((y2 - y1) * (x2 - x1) + 1)
