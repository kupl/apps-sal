(left1, left2, right1, right2) = map(int, input().split())
if right1 + right2 > left1 + left2:
    print('Right')
elif right1 + right2 < left1 + left2:
    print('Left')
else:
    print('Balanced')
