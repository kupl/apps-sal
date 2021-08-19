S = []
res = 'NO'
for i in range(4):
    S.append(list(map(int, input().split())))
for i in range(4):
    p = sum(S[i]) - S[i][3] + S[(i + 1) % 4][0] + S[(i + 2) % 4][1] + S[(i + 3) % 4][2]
    if p > 0 and S[i][3] == 1:
        res = 'YES'
        break
print(res)
