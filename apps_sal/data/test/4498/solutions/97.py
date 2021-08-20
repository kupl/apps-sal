(a, b, c, d) = map(int, input().split())
distance_ab = abs(a - b)
distance_bc = abs(b - c)
distance_ac = abs(a - c)
if distance_ab <= d and distance_bc <= d:
    print('Yes')
elif distance_ac <= d:
    print('Yes')
else:
    print('No')
