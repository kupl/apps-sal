from collections import deque
x,y,a,b,c = map(int,input().split())
ls = []
la = list(map(int,input().split()))
lb = list(map(int,input().split()))
lc = list(map(int,input().split()))
la.sort(reverse=True)
lb.sort(reverse=True)
lc.sort(reverse=True)
for i in range(a):
    ls.append([la[i],1])
for j in range(b):
    ls.append([lb[j],2])
for l in range(c):
    ls.append([lc[l],3])
ls.sort(key=lambda x:x[0],reverse=True)
ls = deque(ls)
s,t,k = 0,0,0
cnt = 0
while True:
    now = ls.popleft()
    if now[1] == 1:
        if s < x:
            cnt += now[0]
            s += 1
    elif now[1] == 2:
        if t < y:
            cnt += now[0]
            t += 1
    else:
        cnt += now[0]
        k += 1
    if s + t + k == x + y:
        print(cnt)
        break
