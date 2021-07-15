import math

X, K, D = list(map(int, input().split()))
X = int(math.fabs(X))

if K < X//D:
    ans = (X - K*D)
else:
    dis = X - D * (X // D)
    if (K-X//D)&1:
        ans = (dis-D)
    else:
        ans = (dis)

print((int(math.fabs(ans))))

