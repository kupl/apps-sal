t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = list(map(int, input().split()))
    print((x2-x1)*(y2-y1)+1)

