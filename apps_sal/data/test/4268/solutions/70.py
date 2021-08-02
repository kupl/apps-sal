import math
N, D = map(int, input().split())
X = []
ans = 0
for i in range(N):
    X.append(list(map(int, input().split())))
for i in range(N):
    for j in range(i + 1, N):
        lis_1 = X[i]
        lis_2 = X[j]
        cnt = 0
        for k in range(D):
            cnt += (lis_1[k] - lis_2[k]) ** 2
        cnt = math.sqrt(cnt)
        if cnt.is_integer():
            ans += 1
print(ans)
