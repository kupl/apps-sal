X,N = map(int,input().split())
P = list(map(int,input().split()))

ans = 0
for a in range(X+1):
    for s in [-1,+1]:
        ans = X + s * a
        if P.count(ans) == 0:
            print(ans)
            return
