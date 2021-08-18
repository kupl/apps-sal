a = list(map(int, input().split()))
z = 998244353
print(a[0] * (a[0] + 1) * (a[1] + 1) * a[1] * a[2] * (a[2] + 1) // 8 % z)
