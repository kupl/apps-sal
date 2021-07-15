S=input()
n=len(S)
if n%2:
    m=n//2
    t=S[m]
    for i in range(m):
        if S[m+i+1]!=t or S[m-i-1]!=t:
            a=m+i+1
            break
    else:
        a=n
else:
    m=n//2
    t=S[m]
    for i in range(m):
        if S[m+i]!=t or S[m-i-1]!=t:
            a=m+i
            break
    else:
        a=n
print(a)
