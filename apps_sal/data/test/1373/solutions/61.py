from scipy.special import comb
n, k = list(map(int, input().split()))
num, ans = 0, 0

for i in range(n + 1):
    num += n - 2 * i
    if i >= k - 1:
        ans += num + 1
ans = ans % (10**9 + 7)
print(ans)
