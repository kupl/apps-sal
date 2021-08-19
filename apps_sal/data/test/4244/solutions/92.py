N = int(input())
X = list(map(int, input().split()))
min_X = min(X)
max_X = max(X)
ans = []
for i in range(min_X, max_X + 1):
    score = []
    for j in range(N):
        score.append((X[j] - i) ** 2)
    ans.append(sum(score))
print(min(ans))
