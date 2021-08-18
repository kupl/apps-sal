H, W = map(int, input().split())
a = ["" for i in range(H)]
for i in range(H):
    a[i] = list(str(input()))

for s in range(-1, H + 1):
    for t in range(-1, W + 1):
        if s == -1 or s == H:
            print("
            break
        else:
            if t == -1:
                print("
            elif t == W:
                print("
            else:
                print(a[s][t], end="")
