(a, b, c) = list(map(int, input().split()))
su = (a + 1) * a // 2 * ((b + 1) * b // 2) * ((c + 1) * c // 2)
ans = su % 998244353
print(int(ans))
