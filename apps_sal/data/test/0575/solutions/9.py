n = int(input())
ax, ay = list(map(int, input().split()))
bx, by = list(map(int, input().split()))
cx, cy = list(map(int, input().split()))

if (bx > ax, by > ay) != (cx > ax, cy > ay):
    print("NO")
    return

print("YES")
