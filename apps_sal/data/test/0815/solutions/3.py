(v1, v2, v3, vm) = [int(i) for i in input().split()]
f = False
for w1 in range(v1, 2 * v1 + 1):
    for w2 in range(v2, 2 * v2 + 1):
        for w3 in range(v3, 2 * v3 + 1):
            if not f and w1 > w2 > w3 and (vm <= w3) and (vm * 2 >= w3) and (vm * 2 < w2) and (vm * 2 < w1):
                print(w1)
                print(w2)
                print(w3)
                f = True
if not f:
    print(-1)
