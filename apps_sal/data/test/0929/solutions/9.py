H, W = map(int, input().split())
A = [list(map(int, input().split()))for _ in range(H)]

ans = []
i = j = 0
while i < H:
    if i % 2 == 0:
        if 0 <= j < W - 1:
            if A[i][j] % 2:
                ans.append([i + 1, j + 1, i + 1, j + 2])
                A[i][j + 1] += 1
            j += 1
        else:
            i += 1
            if i < H:
                if A[i - 1][j] % 2:
                    ans.append([i, j + 1, i + 1, j + 1])
                    A[i][j] += 1
    else:
        if 0 < j:
            if A[i][j] % 2:
                ans.append([i + 1, j + 1, i + 1, j])
                A[i][j - 1] += 1
            j -= 1
        else:
            i += 1
            if i < H:
                if A[i - 1][j] % 2:
                    ans.append([i, j + 1, i + 1, j + 1])
                    A[i][j] += 1

print(len(ans))
for a, b, c, d in ans:
    print(a, b, c, d)
