import sys
N,K = map(int,input().split())
lsx = list(map(int,input().split()))
if 0 in lsx:
    K = K-1
    lsx.remove(0)
if bool(lsx) == False or K == 0:
    print(0)
    return
lshu = []
sei = len(lsx)
for i in range(len(lsx)):
    if lsx[i] < 0:
        lshu.append(lsx[i])
    else:
        sei = i
        break
lssei = lsx[sei:]
lenhu = len(lshu)
lensei = len(lssei)
lshu2 = [abs(lshu[i]) for i in range(lenhu-1,-1,-1)]
dishu = [0] + lshu2
dissei = [0] + lssei
ans = 10*10**8
for i in range(K+1):
    if i <= lenhu and K-i <= lensei:
        ans = min(ans,2*dishu[i]+dissei[K-i],dishu[i]+2*dissei[K-i])
print(ans)
