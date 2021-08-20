import math
(N, X) = list(map(int, input().split()))
a = list(map(int, input().split()))
a.append(X)
a.sort()
S = []
for i in range(N):
    S.append(a[i + 1] - a[i])
ans = S[0]
for j in range(1, N):
    ans = math.gcd(ans, S[j])
print(ans)
