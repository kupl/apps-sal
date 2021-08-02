n = int(input())
bx, by = list(map(int, input().split()))
ax, ay = list(map(int, input().split()))
cx, cy = list(map(int, input().split()))
if (min(ax, cx) <= bx and bx <= max(ax, cx)):
    print("NO")
elif (min(ay, cy) <= by and by <= max(ay, cy)):
    print("NO")
else:
    print("YES")
