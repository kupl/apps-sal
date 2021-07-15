n = int(input())
bx, by = list(map(int, input().split()))
ax, ay = list(map(int, input().split()))
cx, cy = list(map(int, input().split()))
num1 = ax > bx
num3 = cx > bx
num2 = ay > by
num4 = cy > by
if num1 == num3 and num2 == num4:
    print("YES")
else:
    print("NO")

