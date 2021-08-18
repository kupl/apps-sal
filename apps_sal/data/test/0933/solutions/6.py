3


def readln(): return tuple(map(int, input().split()))


cnt = []
for s in list(input() + '
    if cnt == [] or cnt[-1][0] != s:
        cnt.append([s, 1])
    else:
        cnt[-1][1] += 1
ans=[]
tmp=[]
for s, c in cnt:
    if c == 1:
        for _ in range(len(tmp)):
            if _ % 2 == 0:
                ans.append(tmp[_] * 2)
            else:
                ans.append(tmp[_])
        ans.append(s)
        tmp=[]
    else:
        tmp.append(s)
print(''.join(ans[:-1]))
