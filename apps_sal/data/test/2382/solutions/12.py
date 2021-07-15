N=int(input())
S=list(map(int,input().split()))
S.sort()
p=[S[-1]]
r=S[:-1]

for i in range(N):
    nr = []
    for p_ in p[::-1]:
        while r:
            nr.append(r.pop())
            if nr[-1]<p_:
                p.append(nr.pop(-1))
                break
    p.sort()
    r+=nr[::-1]

print("Yes" if len(r)==0 else "No")
