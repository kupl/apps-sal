n, d = list(map(int, input().split()))
down = d
left = -d
right = d
up = 2 * n - d
t = int(input())
for i in range(t):
    x, y = list(map(int, input().split()))
    x, y = x - y, x + y
    if left <= x <= right and down <= y <= up:
        print("YES")
    else:
        print("NO")
    

