(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
t = list(map(int, input().split()))
ans = sum([a[i] for i in range(n) if t[i] == 1])
z = [i for i in range(n) if t[i] == 0]
ln = len(z)
d = 0
now = 0
(left, right) = (0, -1)
for i in range(2 * ln):
    if right + 1 < ln and z[right + 1] - z[left] < k:
        right += 1
        now += a[z[right]]
        d = max(d, now)
    else:
        now -= a[z[left]]
        left += 1
print(ans + d)
