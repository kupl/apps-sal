X, K, D = map(int, input().split())

if abs(X) > K * D:
    print(abs(X) - K * D)
    return

y = abs(X) // D
X_ = abs(X) - y * D
z = K - y
if z % 2 == 0:
    ans = X_
else:
    ans = abs(X_ - D)

print(ans)
