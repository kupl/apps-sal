H, W = list(map(int, input().split()))
masu = [["." for _ in range(W + 2)] for _ in range(H + 2)]

for i in range(H):
    masu[i + 1][1:W + 1] = input()

result = [[0 for _ in range(W)] for _ in range(H)]
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if masu[i][j] == '#':
            x = masu[i - 1][j] + masu[i][j - 1] + masu[i][j + 1] + masu[i + 1][j]
            if x.count("#") == 0:
                print("No")
                return

print("Yes")
