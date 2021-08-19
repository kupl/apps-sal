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
#import numpy as np
#s = np.array(s)
ans = 100100100
for i in range(tdiv):
    lis = []
    # tmp=np.zeros(w)
    # tmp+=s[0,:]
    tmp = [s[0][ii] for ii in range(w)]
    cnt = 0
    # print(tmp)
    for j in range(h - 1):
        if (i >> j & 1):
            # tmp+=s[j+1,:]
            tmp = [tmp[ii] + s[j + 1][ii] for ii in range(w)]
        else:
            lis.append(tmp)
            # tmp=np.zeros(w)
            # tmp+=s[j+1,:]
            tmp = [s[j + 1][ii] for ii in range(w)]
            cnt += 1
    lis.append(tmp)
    #lis = np.array(lis)
    # clis=np.zeros(cnt+1)
    clis = [0 for ii in range(cnt + 1)]
    # print(lis,cnt)
    tmpcnt = cnt
    for ind in range(w):
        # if any(d>k for d in lis[:,ind]):
        # if lis[:,ind].max()>k:
        if max([lis[ii][ind] for ii in range(tmpcnt + 1)]) > k:
            cnt = 10010010
            break
        clis = [lis[ii][ind] + clis[ii] for ii in range(tmpcnt + 1)]
        # if clis.max()>k:
        if max(clis) > k:
            clis = [lis[ii][ind] for ii in range(tmpcnt + 1)]
            cnt += 1
    # print(cnt)
    ans = min(ans, cnt)
print(ans)
# pypyを使おう!
