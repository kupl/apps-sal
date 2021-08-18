import sys

H, W = list(map(int, input().split()))
S = [list(sys.stdin.readline().strip()) for _ in range(H)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i, row in enumerate(S):
    for j, s in enumerate(row):
        if s == ".":
            continue
        ok = False
        for k in range(4):
            nx = j + dx[k]
            ny = i + dy[k]
            if not(0 <= nx < W and 0 <= ny < H):
                continue
            if S[ny][nx] == "#":
                ok = True
        if ok is False:
            print("No")
            return

print("Yes")
