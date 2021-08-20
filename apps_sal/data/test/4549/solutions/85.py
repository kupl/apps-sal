(h, w) = map(int, input().split())
c = tuple((tuple((0 if i == '.' else 1 for i in input())) for _ in range(h)))
for i in range(h):
    for j in range(w):
        if c[i][j]:
            T = c[i - 1][j] if 0 <= i - 1 else 0
            B = c[i + 1][j] if i + 1 < h else 0
            L = c[i][j - 1] if 0 <= j - 1 else 0
            R = c[i][j + 1] if j + 1 < w else 0
            if not (T or B or L or R):
                print('No')
                break
    else:
        continue
    break
else:
    print('Yes')
