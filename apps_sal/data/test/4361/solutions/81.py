n, k = map(int, input().split())
h_l = sorted([int(input()) for _ in range(n)])
ans = float('inf')
for i in range(n - k + 1):
    ans = min(h_l[i + k - 1] - h_l[i], ans)
print(ans)
