from math import ceil
n, k = list(map(int, input().split()))

if k > 0 and k < n:
    ans1 = 1
else:
    ans1 = 0
if k >= ceil(n / 3):
    ans2 = n - k
else:
    ans2 = 2 * k

print(ans1, ans2)
