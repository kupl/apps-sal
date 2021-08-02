n, m = map(int, input().split())
a = [0] * (n + 1)
j = 1
b = [0]
for i in input().split():
    a[j] += int(i) + a[j - 1]
    j += 1
b.extend(list(map(int, input().split())))
b.append(0)

x = int(input())
ans = 0

for i in range(1, n + 1):
    k1 = 10**9
    for j in range(0, n - i + 1):
        k1 = min(k1, a[j + i] - a[j])

    l = r = 1
    k2 = b[1]
    while r <= m:
        if k1 * k2 <= x:
            ans = max(ans, (i) * (r - l + 1))
            r += 1
            k2 += b[r]

        else:
            k2 -= b[l]
            l += 1
print(ans)
