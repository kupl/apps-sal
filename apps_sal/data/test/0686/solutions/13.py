t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    if x - y == 1:
        print("NO")
    else:
        print("YES")
