n=int(input())
a=list(map(int,input().split()))
s=sum(a)
m=max(a)
while True:
    if n*m-s>s:
        print(m)
        break
    else:
        m+=1
