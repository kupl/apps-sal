import math
import itertools
N, D = map(int, input().split())
X = [0] * N
for i in range(N):
    X[i] = list(map(int, input().split()))

cnt = 0
for i in list(itertools.combinations(X, 2)):
    ans = 0
    for j in range(D):
        ans += abs((i[0][j] - i[1][j])**2)
    if math.sqrt(ans).is_integer():
        cnt += 1
print(cnt)
