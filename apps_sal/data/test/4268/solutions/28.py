def dist(a, b):
    ans = 0
    for i in range(D):
        ans += (b[i] - a[i]) ** 2
    ans **= 0.5
    return ans


(N, D) = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
count = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if dist(X[i], X[j]).is_integer():
            count += 1
print(count)
