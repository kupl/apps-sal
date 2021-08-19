(n, k) = map(int, input().split())
P = list(map(int, input().split()))
P[0] = (P[0] + 1.0) / 2
for i in range(1, len(P)):
    P[i] = (P[i] + 1.0) / 2
    P[i] = P[i - 1] + P[i]
ans = 0.0
if n == 1:
    ans = P[0]
elif len(P) - k == 0:
    ans = P[k - 1]
else:
    for i in range(len(P) - k):
        ans = max(ans, P[i + k] - P[i])
print(ans)
