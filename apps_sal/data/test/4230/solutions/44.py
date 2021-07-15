from bisect import bisect

x,n=map(int,input().split())
p=list(map(int,input().split()))

for i in range(100):
    if not(x-i in p):
        print(x-i)
        break
    if not(x+i in p):
        print(x+i)
        break
