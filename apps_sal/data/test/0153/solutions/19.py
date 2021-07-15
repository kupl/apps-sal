n,k,m = list(map(int,input().split()))
t = list(map(int,input().split()))
t.sort()
s = sum(t)
mmm = 0
for i in range(n+1):
    if i*s > m : break
    tm = m-i*s
    c = k*i+i
    for j in range(k):
        c+=min(tm//t[j],n-i)
        tm-=min(tm//t[j],n-i)*t[j]
    mmm = max(mmm,c)
print(mmm)
