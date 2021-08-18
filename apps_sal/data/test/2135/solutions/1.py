
def string2d(arr):
    return ('\n'.join(' '.join(map(str, row)) for row in arr))


H, W = list(map(int, input().split()))
grid = [[c == '.' for c in input()] for i in range(H)]

blah1 = [[0 for j in range(W)] for i in range(H)]
blah2 = [[0 for j in range(W)] for i in range(H)]

for i in range(H):
    for j in range(W):
        if not grid[i][j]:
            continue
        if j + 1 < W and grid[i][j + 1]:
            blah1[i][j] = 1
        if i + 1 < H and grid[i + 1][j]:
            blah2[i][j] = 1

pref1 = [[0 for j in range(W + 1)] for i in range(H + 1)]
pref2 = [[0 for j in range(W + 1)] for i in range(H + 1)]

for i in range(1, H + 1):
    for j in range(1, W + 1):
        pref1[i][j] = pref1[i - 1][j] + blah1[i - 1][j - 1]
        pref2[i][j] = pref2[i - 1][j] + blah2[i - 1][j - 1]
for i in range(1, H + 1):
    for j in range(1, W + 1):
        pref1[i][j] += pref1[i][j - 1]
        pref2[i][j] += pref2[i][j - 1]


Q = int(input())
for q in range(Q):
    r1, c1, r2, c2 = list(map(int, input().split()))
    one = pref1[r2][c2 - 1] - pref1[r2][c1 - 1] - pref1[r1 - 1][c2 - 1] + pref1[r1 - 1][c1 - 1]
    two = pref2[r2 - 1][c2] - pref2[r2 - 1][c1 - 1] - pref2[r1 - 1][c2] + pref2[r1 - 1][c1 - 1]
    print(one + two)
