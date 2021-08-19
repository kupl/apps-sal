a, b, c, d = map(int, input().split())
#print(a, b, c, d)

distance_ab = abs(a - b)
distance_bc = abs(b - c)
distance_ac = abs(a - c)

# aとcが間接的に話せる。
if distance_ab <= d and distance_bc <= d:
    print('Yes')
    # aとcが直接話せる。
elif distance_ac <= d:
    print('Yes')
else:
    print('No')
