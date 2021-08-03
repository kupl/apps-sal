N = int(input())
S = [input() for i in range(3)]
bu = []
for s in S:
    cnt = {}
    mx = 0
    for c in s:
        if c not in cnt:
            cnt[c] = 0
        cnt[c] += 1
        mx = max(mx, cnt[c])
    if mx == len(s) and N == 1:
        bu.append(mx - 1)
    else:
        bu.append(min(len(s), mx + N))

ans = -1
ansmx = -1
for i in range(3):
    if bu[i] > ansmx:
        ans = i
        ansmx = bu[i]
    elif bu[i] == ansmx:
        ans = -1

if ans == -1:
    print('Draw')
elif ans == 0:
    print('Kuro')
elif ans == 1:
    print('Shiro')
else:
    print('Katie')
