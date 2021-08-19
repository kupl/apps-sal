(X, K, D) = map(int, input().split())
a = abs(X) // D
b = abs(X) % D
ans = 0
if a > K:
    ans = abs(X) - D * K
elif (K - a) % 2 == 0:
    ans = b
else:
    ans = abs(b - D)
print(ans)
