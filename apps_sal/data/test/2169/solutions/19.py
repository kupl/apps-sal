H, W, D = list(map(int,input().split()))
d = {}
for i in range(1, H+1):
    A = list(map(int,input().split()))
    for j in range(W):
        d[A[j]] = (i, j+1)
acc = [[] for _ in range(D)]
for i in range(1, D+1):
    acc[i-1].append(0)
    for j in range(i, H*W+1-D, D):
        x,y = d[j]
        a,b = d[j+D]
        #print("po:",j, j+D)
        acc[i-1].append(acc[i-1][-1]+abs(a-x)+abs(b-y))
    
Q = int(input())
for _ in range(Q):
    l, r = list(map(int,input().split()))
    print((acc[(l-1)%D][(r-1)//D]-acc[(l-1)%D][(l-1)//D]))

