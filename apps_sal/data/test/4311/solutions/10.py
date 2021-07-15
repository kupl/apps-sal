n=int(input())
a=[n]
cnt=1
while len(set(a))==len(a):
    if n%2==0: 
        n//=2
    else:
        n=3*n+1
    a.append(n)
    cnt+=1
print(cnt)

