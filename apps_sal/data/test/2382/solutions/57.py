N=int(input())
S=list(map(int,input().split()))
S.sort()
p=S[-1:]
r=S[:-1]
for i in range(N):
    nr=[]
    for p_ in p[::-1]:
        while r:
            r_=r.pop()
            if r_<p_:
                p.append(r_)
                break
            nr.append(r_)
    p.sort()
    r+=nr[::-1]
print("Yes" if len(r)==0 else "No")
