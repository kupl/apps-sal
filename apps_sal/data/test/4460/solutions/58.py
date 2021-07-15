a=list(map(int,input().split()))
t=0
s=0
for i in range(len(a)):
    t=t+1
    if a[i]!=i+1:
     s=t
print(s)
