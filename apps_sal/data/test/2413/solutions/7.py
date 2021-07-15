t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    ma = n
    st=-1
    f=-1
    for j in range(n):
        if s[j]=='1':
            st=j
            break
    for j in range(n-1, -1, -1):
        if s[j]=='1':
            f = j
            break
    if f!=-1:
        ma=max(ma, (f+1)*2)
        ma=max(ma, (n-st)*2)
    print(ma)

