a=list(map(int,input().split()))
m=max(a)*3-sum(a)
if m%2==1:
    m+=3
print(m//2)
