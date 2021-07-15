import bisect
A,B,Q=map(int,input().split())
s=[-10**15]
t=[-10**15]
ans=[]
for _ in range(A):
    s.append(int(input()))
for _ in range(B):
    t.append(int(input()))
s.append(10**15)
t.append(10**15)
def search(a,b,q):
    dis=10**15
    S=[s[a-1],s[a]]
    T=[t[b-1],t[b]]
    for i in range(2):
        for j in range(2):
            A=min(abs(S[i]-q),abs(T[j]-q))+abs(S[i]-T[j])
            dis=min(dis,A)
    return dis
for _ in range(Q):
    q=int(input())
    r=bisect.bisect_left(s,q)
    l=bisect.bisect_left(t,q)
    ans.append(search(r,l,q))
for i in ans:
    print(i)
