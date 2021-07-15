n = int(input())
h = list(map(str, input().rstrip().split()))
ans = '_'
nuls = 0
for i in range(len(h)):
    if h[i][0] == '0':
        ans = '0'
        break
    else:
        cnt = 0
        for j in range(len(h[i])):
            if (h[i][j] == '0'):
                cnt += 1
        if (cnt == len(h[i]) - 1 and h[i][0] == '1'):
            nuls += cnt
        else:
            ans = h[i]
if (ans == '0'):
    print(ans)
else:
    if (ans == '_'):
        ans = '1'
    for i in range(nuls):
        ans += '0'
    print(ans)
