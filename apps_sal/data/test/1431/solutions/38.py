import sys,math,collections,itertools
input = sys.stdin.readline

N = int(input())
a = list(map(int,input().split()))
a.insert(0,0)
b = []
c = [0 for _ in range(N+1)]
for i in range(N,0,-1):
    cnt = 0
    for j in range(2*i,N+1,i):
        if c[j] == 1:
            cnt +=1
    if (cnt%2==1 and a[i] == 0) or (cnt%2==0 and a[i] == 1):
        b.append(i)
        c[i] = 1
print((len(b)))
print((*b))

