#40 C - Streamline
N,M = map(int,input().split())
X = list(map(int,input().split()))
X = sorted(X,reverse = False)

# 区間の距離のリスト
if len(X) == 1:
    print(0)
else:
    dist = []
    for i in range(1,M):
        dist.append(X[i]-X[i-1])
    dist = sorted(dist,reverse = False)
    # 区間の距離を降順に N-1 個分消去
    for k in range(N-1):
        dist.pop()
        if len(dist) == 0:
            break
    print(sum(dist))
