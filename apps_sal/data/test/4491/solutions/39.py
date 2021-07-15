n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
for i in range(n):
    c=max(sum(a[:i+1])+sum(b[i:]),c)
print(c)
