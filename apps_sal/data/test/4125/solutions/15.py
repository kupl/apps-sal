import math
N, X = map(int, input().split())
x = list(map(int, input().split()))
x.append(X)
x.sort()
diff = [x[i + 1] - x[i] for i in range(N)]

ans = diff[0]

for i in range(1, N):
    ans = math.gcd(ans, diff[i])

print(ans)
