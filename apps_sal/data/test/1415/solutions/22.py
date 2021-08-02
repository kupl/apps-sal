rs, cs, r, c = map(int, input().split())
s = input()
r -= 1
c -= 1

f = [[0] * cs for i in range(rs)]
res = [0] * len(s)
cnt = 0

for i in range(len(s)):
    if f[r][c] == 0:
        res[i] = 1
        cnt += 1
        f[r][c] = 1

    if s[i] == 'U' and r > 0:
        r -= 1
    elif s[i] == 'R' and c < cs - 1:
        c += 1
    elif s[i] == 'D' and r < rs - 1:
        r += 1
    elif s[i] == 'L' and c > 0:
        c -= 1

print(' '.join(map(str, res)), rs * cs - cnt)
