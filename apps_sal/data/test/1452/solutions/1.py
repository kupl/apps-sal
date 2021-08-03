h, w = list(map(int, input().split()))
r = list(map(int, input().split()))
c = list(map(int, input().split()))

a = [[0] * w for i in range(h)]
for i in range(h):
    if r[i] < w:
        a[i][:r[i] + 1] = [1] * r[i] + [-1]
    else:
        a[i] = [1] * w
for j in range(w):
    for i in range(c[j]):
        if a[i][j] == -1:
            print(0)
            break
        a[i][j] = 1
    else:
        if c[j] < h:
            if a[c[j]][j] == 1:
                print(0)
                break
            a[c[j]][j] = -1
        continue
    break
else:
    cnt0 = sum([row.count(0) for row in a])
    print(2 ** cnt0 % 1000000007)
