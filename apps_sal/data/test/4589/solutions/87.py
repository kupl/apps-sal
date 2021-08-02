h, w = map(int, input().split())
m = []

for i in range(h):
    m.append(input())

ans = [["#"] * (w) for _ in range(h)]
for i in range(h):
    for j in range(w):
        cnt = 0
        if h > i - 1 >= 0:
            if m[i - 1][j] == "#":
                cnt += 1
            if w > j - 1 >= 0 and m[i - 1][j - 1] == "#":
                cnt += 1
            if w > j + 1 >= 0 and m[i - 1][j + 1] == "#":
                cnt += 1
        if h > i + 1 >= 0:
            if m[i + 1][j] == "#":
                cnt += 1
            if w > j - 1 >= 0 and m[i + 1][j - 1] == "#":
                cnt += 1
            if w > j + 1 >= 0 and m[i + 1][j + 1] == "#":
                cnt += 1

        if w > j - 1 >= 0 and m[i][j - 1] == "#":
            cnt += 1
        if w > j + 1 >= 0 and m[i][j + 1] == "#":
            cnt += 1
        if m[i][j] != "#":
            ans[i][j] = str(cnt)

for i in range(h):
    print("".join(ans[i]))
