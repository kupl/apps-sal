(k, a, b) = list(map(int, input().split()))
below_a = a // k
below_b = b // k
ans = below_b - below_a
if a % k == 0:
    ans += 1
print(ans)
