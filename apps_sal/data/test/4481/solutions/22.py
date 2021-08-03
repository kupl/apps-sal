
n = int(input())
l = [str(input()) for i in range(n)]

l = sorted(l)

cnt = 1
cnt_max = 1
moji = []

for i in range(1, n):
    if l[i] == l[i - 1]:
        cnt += 1
        if i == n - 1:
            if cnt_max < cnt:
                cnt_max = cnt
                moji = [l[i - 1]]
            elif cnt_max == cnt:
                moji.append(l[i - 1])
    else:
        if cnt_max < cnt:
            cnt_max = cnt
            moji = [l[i - 1]]
        elif cnt_max == cnt:
            moji.append(l[i - 1])
            if cnt_max == 1 and i == n - 1:
                moji.append(l[i])
        cnt = 1

for i in range(len(moji)):
    print((moji[i]))
