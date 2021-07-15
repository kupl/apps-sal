N,K = map(int,input().split())
ls = [0]
for i in range(1,N+1):
    if i >= K:
        ls.append(1)
    else:
        p = 1
        f = K//i
        if K%i == 0:
            f -= 1
        while f != 0:
            f = f//2
            p = p/2
        ls.append(p)
ans = sum(ls)/N
print(ans)
