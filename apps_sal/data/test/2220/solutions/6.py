(n, m, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
k1 = a[-1]
k2 = a[-2]
x = m // (k + 1)
ans = k2 * x + (m - x) * k1
print(ans)
