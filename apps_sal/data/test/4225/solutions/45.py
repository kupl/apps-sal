(a, b, c, k) = list(map(int, input().split()))
ans = min(a, k)
k = max(0, k - a - b)
ans -= k
print(ans)
