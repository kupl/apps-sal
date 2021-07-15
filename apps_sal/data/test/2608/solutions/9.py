t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    count_w = n * m // 2 + n * m % 2
    count_g = n * m // 2
    if (x1 + y1) % 2 == 0:
        count_g -= (x2 - x1 + 1) * (y2 - y1 + 1) // 2
        count_w += (x2 - x1 + 1) * (y2 - y1 + 1) // 2
    else:
        count_g -= (x2 - x1 + 1) * (y2 - y1 + 1) // 2 + (x2 - x1 + 1) * (y2 - y1 + 1) % 2
        count_w += (x2 - x1 + 1) * (y2 - y1 + 1) // 2 + (x2 - x1 + 1) * (y2 - y1 + 1) % 2
    x5 = max(x1, x3)
    x6 = min(x4, x2)
    y5 = max(y1, y3)
    y6 = min(y4, y2)
    if (x3 + y3) % 2 == 1:
        count_g += (x4 - x3 + 1) * (y4 - y3 + 1) // 2
        count_w -= (x4 - x3 + 1) * (y4 - y3 + 1) // 2
    else:
        count_g += (x4 - x3 + 1) * (y4 - y3 + 1) // 2 + (x4 - x3 + 1) * (y4 - y3 + 1) % 2
        count_w -= (x4 - x3 + 1) * (y4 - y3 + 1) // 2 + (x4 - x3 + 1) * (y4 - y3 + 1) % 2
    if (x5 + y5) % 2 == 0 and x5 <= x6 and y5 <= y6:
        count_g += (x6 - x5 + 1) * (y6 - y5 + 1) // 2
        count_w -= (x6 - x5 + 1) * (y6 - y5 + 1) // 2
    elif x5 <= x6 and y5 <= y6:
        count_g += (x6 - x5 + 1) * (y6 - y5 + 1) // 2 + (x6 - x5 + 1) * (y6 - y5 + 1) % 2
        count_w -= (x6 - x5 + 1) * (y6 - y5 + 1) // 2 + (x6 - x5 + 1) * (y6 - y5 + 1) % 2
    print(count_w, count_g)
