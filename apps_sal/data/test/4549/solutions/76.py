h, w = map(int, input().split())
a = [input() + '.' for i in range(h)] + ['.' * w]
for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            if any([a[i + 1][j] == a[i][j + 1] == a[i - 1][j] == a[i][j - 1] == "."]):
                print('No')
                break
    else:
        continue
    break
else:
    print('Yes')
