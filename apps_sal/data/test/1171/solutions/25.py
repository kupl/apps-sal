N,K = map(int,input().split())
V = list(map(int,input().split()))

ans = -1

for l in range(N+1):
    for r in range(N+1):
        tmp = V[:l] + V[N-r:]
        if l+r > N:
            break
        res = K - (l+r)
        if res < 0:
            break
        tmp.sort()
        for i in range(min(res,len(tmp))):
            if tmp[0] < 0:
                tmp.pop(0)
            else:
                break
        ans = max(ans,sum(tmp))
            
print(ans)
