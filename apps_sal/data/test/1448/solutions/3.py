n, d = list(map(int, input().split()))
m = int(input())
n2d = n * 2 - d
for _ in range(m):
    x, y = list(map(int, input().split()))
    if n2d >= x + y >= d and abs(x - y) <= d:
        print("YES")
    else:
        print("NO")
