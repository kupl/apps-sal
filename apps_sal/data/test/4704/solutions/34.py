from itertools import accumulate
n = int(input())
a = list(map(int, input().split()))
a = list(accumulate(a))
ans = 10 ** 10
for i in range(n - 1):
    ans = min(ans, abs(a[i] - a[-1] + a[i]))
print(ans)
