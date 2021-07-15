N,K = map(int,input().split())
cnt = 0
for x in range(2,2*N+1):
    if 2<=x-K<=2*N:
        y = x-K
        if x-1>=N:
            c1 = max(x-1-2*(x-1-N),0)
        else:
            c1 = x-1
        if y-1>=N:
            c2 = max(y-1-2*(y-1-N),0)
        else:
            c2 = y-1
        cnt += c1*c2
print(cnt)
