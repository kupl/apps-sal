n, m, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
r = m // (k + 1)
ans = a[-1] * (r * k + (m % (k + 1))) + a[-2] * r
print(ans)
