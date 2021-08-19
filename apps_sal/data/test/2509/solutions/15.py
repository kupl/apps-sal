n, k = map(int, input().split())

# ans = 0
# for right in range(k+1, n+1):
#     for left in range(max(1,k), right):
#         while left <= n:
#             ans+=1
#             left+=right
# print(ans, flush=True)
# TLE

ans = 0
for b in range(1, n + 1):
    ans += (n // b) * max(0, b - k) + max(n % b + 1 - k, 0)
    if k == 0:
        ans -= 1
print(ans, flush=True)
