X, K, D = list(map(int, input().split()))
ans = abs(X)
rem = K
k = min(ans // D, K)
ans -= k * D
rem -= k
if rem > 0:
    if rem % 2 == 1:
        ans = ans - D
print((abs(ans)))
