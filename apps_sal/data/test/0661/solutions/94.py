m, k = map(int, input().split())
v = []
if k == 0:
    for i in range(0, 2**m):
        v.append(i)
        v.append(i)
elif k < 2**m and m > 1:
    for i in range(0, 2**m):
        if i != k:
            v.append(i)
    v.append(k)
    for i in range(2**m - 1, -1, -1):
        if i != k:
            v.append(i)
    v.append(k)
if len(v) == 0:
    print(-1)
else:
    for i in range(0, len(v)):
        print(v[i])
        if i == len(v) - 1:
            print("\n")
        else:
            print(" ")
