n, m, k = list(map(int, input().split()))
a = [int(s) for s in input().split()]
a.sort()
ans = m // (k + 1) * (a[-1] * k + a[-2])
ans += m % (k + 1) * a[-1]
print(ans)
