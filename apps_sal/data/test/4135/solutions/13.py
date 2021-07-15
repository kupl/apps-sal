n=int(input())
t=list(map(str,input()))
for i in range(1,n+1):
    if n%i==0:
        t=t[:i][::-1]+t[i:]
for i in t:
    print(i,end='')

