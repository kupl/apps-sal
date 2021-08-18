import sys


def input():
    return sys.stdin.readline()[:-1]


h, w, k = list(map(int, input().split()))
s = []
for i in range(h):
    str = input()
    tmp = []
    for j in range(w):
        if str[j] == "0":
            tmp.append(0)
        else:
            tmp.append(1)
    s.append(tmp)

tdiv = 2**(h - 1)
ans = 100100100
for i in range(tdiv):
    lis = []
    tmp = [s[0][ii] for ii in range(w)]
    cnt = 0
    for j in range(h - 1):
        if (i >> j & 1):
            tmp = [tmp[ii] + s[j + 1][ii] for ii in range(w)]
        else:
            lis.append(tmp)
            tmp = [s[j + 1][ii] for ii in range(w)]
            cnt += 1
    lis.append(tmp)
    clis = [0 for ii in range(cnt + 1)]
    tmpcnt = cnt
    for ind in range(w):
        if max([lis[ii][ind] for ii in range(tmpcnt + 1)]) > k:
            cnt = 10010010
            break
        clis = [lis[ii][ind] + clis[ii] for ii in range(tmpcnt + 1)]
        if max(clis) > k:
            clis = [lis[ii][ind] for ii in range(tmpcnt + 1)]
            cnt += 1
    ans = min(ans, cnt)
print(ans)
