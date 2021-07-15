from sys import stdin
from sys import setrecursionlimit as SRL; SRL(10**7)
rd = stdin.readline
rrd = lambda: list(map(int, rd().strip().split()))

lat = [chr(ord('a')+i) for i in range(26)]


n,k = rrd()

p = list(rrd())
q = list(rrd())

cnt = [0]*200005

ct = 0

ans = ['a']*n


now = 0
for i in range(n):
    if q[i] == p[i]:
        if ct == 0 and i:
            now += 1
            now = min(now,25)
        ans[q[i]-1] = lat[now]

    else:
        if ct == 0 and i:
            now += 1
            now = min(now,25)

        cnt[q[i]]+=1
        cnt[p[i]]+=1

        if cnt[q[i]] == 2:
            ct -= 1
        else:
            ct += 1
        if cnt[p[i]] == 2:
            ct -= 1
        else:
            ct += 1

        ans[p[i]-1] = lat[now]
        ans[q[i]-1] = lat[now]





if now+1 >= k:
    print("YES")
    print("".join(ans))
else:
    print("NO")






