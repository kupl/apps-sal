from copy import deepcopy
n = int(input())
H = list(map(int, input().split()))
ans = 0
while any(h != 0 for h in H):
    X = list()
    tmp = list()
    for h in H:
        if h != 0:
            X.append(h)
        else:
            if X:
                m = min(X)
                tmp += list([y - m for y in X])
                ans += m
                X = list()
            tmp+=[0,]
    if X:
        m = min(X)
        tmp += list([y - m for y in X])
        ans += m
        X = list()
    H = deepcopy(tmp)
print(ans)

