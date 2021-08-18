n = int(input())
s = [[0] * 26 for i in range(26)]
for i in range(n):
    tmp = input().strip()
    lel = [0] * 26
    lens = len(tmp)
    for j in tmp:
        lel[ord(j) - ord('a')] = lens
    if lel.count(0) == 24:
        tmp = 0
        for j in range(26):
            if tmp == 0 and lel[j] != 0:
                tmp += 1
                a = j
            if tmp == 1 and lel[j] != 0:
                b = j
        s[a][b] += lens
        s[b][a] += lens
    if lel.count(0) == 25:
        for j in range(26):
            if lel[j] != 0:
                a = j
        for j in range(26):
            s[a][j] += lens
            if j != a:
                s[j][a] += lens
mx = 0
for i in range(26):
    for j in range(26):
        mx = max(mx, s[i][j])
print(mx)
