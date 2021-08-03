X, K, D = list(map(int, input().split()))

X = abs(X)

count = X // D
ans = 0

if count >= K:
    ans = X - (K * D)
else:
    if (K - count) % 2 == 0:
        ans = X - (count * D)
    else:
        ans = X - (count + 1) * D

print((abs(ans)))
