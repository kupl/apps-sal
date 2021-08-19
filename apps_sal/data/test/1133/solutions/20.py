N = int(input())
tbl = [[0] * 26 for x in range(26)]
for n in range(N):
    word = input()
    chrs = [0] * 26
    for c in word:
        chrs[ord(c) - 97] += 1
    stuff = [(i, x) for (i, x) in enumerate(chrs) if x > 0]
    if len(stuff) == 1:
        for a in range(26):
            if a != stuff[0][0]:
                tbl[a][stuff[0][0]] += stuff[0][1]
                tbl[stuff[0][0]][a] += stuff[0][1]
    elif len(stuff) == 2:
        tbl[stuff[0][0]][stuff[1][0]] += stuff[0][1] + stuff[1][1]
        tbl[stuff[1][0]][stuff[0][0]] += stuff[0][1] + stuff[1][1]
ans = 0
for a in range(26):
    for b in range(26):
        ans = max(ans, tbl[a][b])
print(ans)
