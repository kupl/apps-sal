n, d = [int(i) for i in input().split()]
m = int(input())
for i in range(m):
    x, y = [int(i) for i in input().split()]
    if (y >= x - d and y <= x + d and y >= -x + d and y <= -x + 2 * n - d):
        print("YES")
    else:
        print("NO")
