n, d = map(int, input().split())
m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    if (x + y) < d:
        print("NO")
    elif (x + y) > n * 2 - d:
        print("NO")
    elif abs(x - y) > d:
        print("NO")
    else:
        print("YES")
