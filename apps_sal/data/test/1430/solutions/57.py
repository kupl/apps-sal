import itertools
def s(): return input()
def I(): return map(int,input().split())

N,K = I()
S = list(s())
num = 1
cnt = 0
L = []
for i in range(N-1):
    if S[i] != S[i+1]:
        L.append(num)
        num = 0
        if S[i] == '0':
            cnt += 1
    num += 1
L.append(num)
if S[-1] == '0':
    cnt += 1
ruiseki = [0]+list(itertools.accumulate(L))
l = len(ruiseki)
if cnt <= K:
    print(N)
    return
start = 0
ans = 0
if S[0] == '0':
    start = 1
for i in range(start,l,2):
    if i+K*2+1 > l-1:
        break
    ans = max(ans,ruiseki[i+K*2+1]-ruiseki[i])
if S[0] == '0':
    ans = max(ans,ruiseki[K*2])
if S[-1] == '0':
    ans = max(ans,ruiseki[-1]-ruiseki[l-K*2-1])
print(ans)
