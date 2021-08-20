(n, k) = list(map(int, input().split()))
l = list(map(int, input().split()))
ans = 10000000000000
for i in range(n - k + 1):
    ans1 = abs(l[i]) + abs(l[i + k - 1] - l[i])
    ans2 = abs(l[i + k - 1]) + abs(l[i + k - 1] - l[i])
    ans = min(ans, ans1, ans2)
print(ans)
