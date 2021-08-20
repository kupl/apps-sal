(a, b, c) = list(map(int, input().split()))
t = (a + 1) * a * (b + 1) * b * (c + 1) * c // 8
ans = t % 998244353
print(ans)
