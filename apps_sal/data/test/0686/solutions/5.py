n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if abs(x - y) > 1:
        print("YES")
    else:
        print("NO")
