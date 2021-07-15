n=int(input())
a=list(map(int,input().split()))

c=[0]*n

for i in range(len(a)):
    c[a[i]-1]=c[a[i]-1]+1

for i in c:
    print(i)
