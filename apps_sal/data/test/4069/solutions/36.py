X, K, D = map(int, input().split())
X = abs(X)
div, mod = divmod(X, D)
if X > D * K:
    ans = X - D * K
elif (K - div) % 2 == 0:
    ans = mod
else:
    ans = D - mod
print(ans)
