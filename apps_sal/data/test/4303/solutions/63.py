import bisect
n, k = list(map(int, input().split()))
x = list(map(int, input().split()))


b = bisect.bisect_left(x, 0)

r = x[b:]
l = list(reversed(x[:b]))


R = len(r)
L = len(l)

ans = float('inf')

if k <= R:
    ans = min(ans, r[k - 1])

if k <= L:
    ans = min(ans, abs(l[k - 1]))

# 右折り返し
for i in range(R):
    if i < k and k - i - 2 <= L - 1 and k - i - 2 >= 0:
        tmp = 2 * r[i] + abs(l[k - i - 2])
        ans = min(ans, tmp)
# 左折り返し
for j in range(L):
    if j < k and k - j - 2 <= R - 1 and k - j - 2 >= 0:
        tmp = 2 * abs(l[j]) + r[k - j - 2]
        ans = min(ans, tmp)


print(ans)
