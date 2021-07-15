x, y = [0] * 8, [0] * 8
for i in range(8): x[i], y[i] = map(int, input().split())
for i in range(8):
    for j in range(i):
        if x[i] == x[j] and y[i] == y[j]:
            print("ugly")
            break
    else:
        continue
    break
else:        
    x.sort()
    y.sort()
    if (x[0] == x[1] == x[2] and x[3] == x[4] and x[5] == x[6] == x[7] and
        y[0] == y[1] == y[2] and y[3] == y[4] and y[5] == y[6] == y[7] and
        x[2] != x[3] and x[4] != x[5] and y[2] != x[3] and y[4] != x[5]):
        print("respectable")
    else: print("ugly")
