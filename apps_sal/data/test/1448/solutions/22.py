n, d = list(map(int, input().split()))
m = int(input())
for i in range(m):
    x, y = list(map(int, input().split()))
    if y >= d - x and y <= x + d and y >= x - d and y <= -x - d + 2 * n:
        print("YES")
    else:
        print("NO")

