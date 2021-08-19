(n, a) = [int(i) for i in input().split()]
points = [int(i) for i in input().split()]
right = None
right2 = None
left = None
left2 = None
for point in points:
    if right is None:
        right = point
    elif point > right:
        right2 = right
        right = point
    elif right2 is None or point > right2:
        right2 = point
    if left is None:
        left = point
    elif point < left:
        left2 = left
        left = point
    elif left2 is None or point < left2:
        left2 = point
if n == 1:
    print(0)
elif a >= right:
    print(a - left2)
elif a <= left:
    print(right2 - a)
else:
    x1 = abs(a - left) + abs(right2 - left)
    x2 = abs(a - left2) + abs(right - left2)
    x3 = abs(right - a) + abs(right - left2)
    x4 = abs(right2 - a) + abs(right2 - left)
    print(min((x1, x2, x3, x4)))
