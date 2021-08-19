(N, K) = list(map(int, input().split()))
x = list(map(int, input().split()))
positive = []
negative = []
for i in range(N):
    if x[i] < 0:
        negative.append(-x[i])
    else:
        positive.append(x[i])
negative.sort()
n = len(negative)
m = len(positive)
ans = 1000000000
if n >= K:
    ans = min(ans, negative[K - 1])
if m >= K:
    ans = min(ans, positive[K - 1])
for i in range(n):
    j = K - (i + 1)
    if j > m:
        continue
    if j <= 0:
        continue
    ans = min(ans, negative[i] + positive[j - 1] + min(negative[i], positive[j - 1]))
print(ans)
