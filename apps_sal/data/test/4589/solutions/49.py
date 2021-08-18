H, W = map(int, input().split())
m = []

for i in range(H):
    s = input()
    t = []
    for i in s:
        t.append(1 if i == "
    m.append(t)

for i in range(H):
    for j in range(W):
        if m[i][j] == 1:
            print("
            continue
        count=0
        if i != 0:
            count += m[i - 1][j]
            if j != 0:
                count += m[i - 1][j - 1]
            if j != W - 1:
                count += m[i - 1][j + 1]
        if i != H - 1:
            count += m[i + 1][j]
            if j != 0:
                count += m[i + 1][j - 1]
            if j != W - 1:
                count += m[i + 1][j + 1]
        if j != 0:
            count += m[i][j - 1]
        if j != W - 1:
            count += m[i][j + 1]
        print(count, end="")
    print()
