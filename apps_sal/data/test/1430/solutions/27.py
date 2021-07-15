N,K = map(int,input().split())
s = input()
ls = []
i = 0
c = 0
while i < N and s[i] == "1":
    c += 1
    i += 1
if i==N:
    print(N)
    return
while i < N:
    l = c
    c = 0
    while i < N and s[i] == "0":
        c += 1
        i += 1
    m = c
    c = 0
    while i < N and s[i] == "1":
        c += 1
        i += 1
    r = c
    ls.append((l,m,r))
K = min(K, len(ls))
from itertools import accumulate
acc = list(accumulate([0]+ls, lambda x,y:x+y[1]+y[2]))
ans = 0
for i in range(len(ls)-K+1):
    ans = max(ans, acc[i+K]-acc[i]+ls[i][0])
print(ans)
