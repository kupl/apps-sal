n=int(input())
a=list(map(int,input().split()))
h=min(a)
a=a+a
pos=a.index(h)
w=0
for i in range(pos+1,2*n):
    if a[i]==h:
        w=max(w,i-pos-1)
        pos=i
print(h*n+w)
