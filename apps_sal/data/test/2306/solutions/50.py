N = int(input())
T = list(map(int, input().split()))
V = list(map(int, input().split()))

Ttot = sum(T)
Wf = [0]*(Ttot+1)
Wb = [0]*(Ttot+1)

i = 0
w = 0
for t,v in zip(T,V):
    for j in range(t):
        i += 1
        w = min(w+1, v)
        Wf[i] = w

i = 0
w = 0
for t,v in zip(T[::-1],V[::-1]):
    for j in range(t):
        i += 1
        w = min(w+1, v)
        Wb[i] = w

ans = 0
wp = 0
wfp = 0
wbp = Wb[Ttot]
for i in range(1, Ttot+1):
    wf = Wf[i]
    wb = Wb[Ttot-i]
    
    w = min(wf, wb)
    ans += wp + 0.5*(w-wp)
    if wf-wfp==1 and wb-wbp==-1 and w==wp:
        ans += 0.25

    wp = w
    wfp = wf
    wbp = wb

print(ans)
