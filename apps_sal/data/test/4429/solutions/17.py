from itertools import *
for i in range(int(input())):
    x, y, z = list(map(int, input().split()))
    a = [x, y, z, min(x, y, z), max(x, y, z)]
    ha = False
    for p in permutations(a):
        if max(p[0], p[1]) == x and max(p[0], p[2]) == y and max(p[1], p[2]) == z:
            print("YES")
            print(*p[:3])
            ha = True
            break
    if not ha:
        print("NO")
