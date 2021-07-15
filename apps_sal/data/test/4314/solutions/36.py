h,w = list(map(int,input().split()))
masu = []
for i in range(h):
    tmp = str(input())
    masu.append(tmp)

tmp_h = [int(0) for i in range(h)]
tmp_w = [int(0) for j in range(w)]
for i in range(h):
    for j in range(w):
        if masu[i][j]=='.':
            tmp_h[i] += 1
            tmp_w[j] += 1
#print(tmp_h)
#print(tmp_w)

ans = []
for i in range(len(tmp_h)):
    if tmp_h[i] != w:
        tmp = ''
        for j in range(w):
            if tmp_w[j] != h:
                tmp += masu[i][j]
        ans.append(tmp)

#for i in range(h):
#    print(masu[i])
#print('-----')
for i in range(len(ans)):
    print((ans[i]))

