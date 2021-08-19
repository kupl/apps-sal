(k, a, b) = map(int, input().split())
floor_a = a // k
floor_b = b // k
ans = floor_b - floor_a
if a % k == 0:
    ans += 1
print(ans)
