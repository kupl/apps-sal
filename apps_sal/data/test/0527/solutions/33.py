s = input()
t = input()
n = len(s)
s += s
# pos[i][j] := 場所iの次に現れる最も近いj(文字)のインデックス
pos = [[-1] * 26 for _ in range(n * 2 + 1)]
for i in range(n * 2 - 1, -1, -1):
    k = ord(s[i]) - ord('a')
    for j in range(26):
        if j == k:
            pos[i][j] = i
        else:
            pos[i][j] = pos[i + 1][j]

ans = 0
now = 0
for c in t:
    x = ord(c) - ord('a')
    if pos[now][x] == -1:
        print((-1))
        return
    ans += -~pos[now][x] - now
    now = -~pos[now][x] % n
print(ans)

