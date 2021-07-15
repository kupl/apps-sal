n = int(input())
a = list(map(int,input().split()))

c = []

for i in range(1,n+1):
    c.append((i,a[i-1]))

a = sorted(c,key=lambda x:x[1])

for i,idx in a:
    print(i,end=" ")
