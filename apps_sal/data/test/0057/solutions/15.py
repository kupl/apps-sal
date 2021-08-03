n = int(input())
if n == 1:
    print(-1)
elif n == 2:
    x1, y1 = list(map(int, input().split()))
    x2, y2 = list(map(int, input().split()))
    if x1 != x2 and y1 != y2:
        print(abs(x1 - x2) * abs(y1 - y2))
    else:
        print(-1)
elif n == 3:
    x1, y1 = list(map(int, input().split()))
    x2, y2 = list(map(int, input().split()))
    x3, y3 = list(map(int, input().split()))
    if x1 != x2 and y1 != y2:
        print(abs(x1 - x2) * abs(y1 - y2))
    elif x1 != x3 and y1 != y3:
        print(abs(x1 - x3) * abs(y1 - y3))
    else:
        print(abs(x2 - x3) * abs(y2 - y3))
else:
    x1, y1 = list(map(int, input().split()))
    x2, y2 = list(map(int, input().split()))
    x3, y3 = list(map(int, input().split()))
    x4, y4 = list(map(int, input().split()))
    if x1 != x2 and y1 != y2:
        print(abs(x1 - x2) * abs(y1 - y2))
    elif x1 != x3 and y1 != y3:
        print(abs(x1 - x3) * abs(y1 - y3))
    else:
        print(abs(x2 - x3) * abs(y2 - y3))
