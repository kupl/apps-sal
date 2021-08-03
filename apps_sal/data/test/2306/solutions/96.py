n = int(input())
t = [0] + list(map(int, input().split()))
v = [0] + list(map(int, input().split()))

left = [0] * (n + 1)
right = [0] * (n + 1)

for i in range(1, n):
    s = left[i - 1]
    left[i] = min(s + t[i], v[i], v[i + 1])
for i in range(n - 1, 0, -1):
    s = right[i + 1]
    right[i] = min(s + t[i + 1], v[i], v[i + 1])

ad = [min(x, y) for x, y in zip(left, right)]


def cal(le, ri, t, v):
    x = v - le + v - ri
    if x >= t:
        v = (le + ri + t) / 2
        x = t
    d = (le + v) * (v - le) / 2
    d += v * (t - x)
    d += (ri + v) * (v - ri) / 2
    return d


ans = 0
for i in range(1, n + 1):
    ans += cal(ad[i - 1], ad[i], t[i], v[i])
print(ans)
