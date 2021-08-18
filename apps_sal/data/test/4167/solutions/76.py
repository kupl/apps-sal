n, k = list(map(int, input().split()))
n0 = n // k
ans = pow(n0, 3)
if k % 2 == 0:
    r = n % k
    ans += pow(n0 + int(n % k >= k // 2), 3)
print(ans)
