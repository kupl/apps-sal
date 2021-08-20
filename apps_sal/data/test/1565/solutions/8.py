L = int(input())
X = input()
ans = float('inf')
cnt = 0
idx = L // 2
while cnt < 5 and idx >= 1:
    if X[idx] != '0':
        ans = min(ans, int(X[:idx]) + int(X[idx:]))
        cnt += 1
    idx -= 1
cnt = 0
idx = L // 2
while cnt < 5 and idx < L:
    if X[idx] != '0':
        ans = min(ans, int(X[:idx]) + int(X[idx:]))
        cnt += 1
    idx += 1
print(ans)
