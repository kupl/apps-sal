n = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

if bx < ax < cx:
    print("NO")
elif cx < ax < bx:
    print("NO")
elif by < ay < cy:
    print("NO")
elif cy < ay < by:
    print("NO")
else:
    print("YES")
