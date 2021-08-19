from itertools import accumulate
n = int(input())
a = list(map(int, input().split()))
ac = list(accumulate(a))
ans = float('inf')
l = 0
r = 1
for i in range(1, n - 2):
    while abs(ac[i] - 2 * ac[l + 1]) < abs(ac[i] - 2 * ac[l]) and l < i + 1:
        l += 1
    while abs(ac[-1] - 2 * ac[r + 1] + ac[i]) < abs(ac[-1] - 2 * ac[r] + ac[i]) and r < n - 2:
        r += 1
    t = [ac[l], ac[i] - ac[l], ac[r] - ac[i], ac[-1] - ac[r]]
    ans = min(ans, max(t) - min(t))
print(ans)
