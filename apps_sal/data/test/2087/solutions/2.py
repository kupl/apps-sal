l = list(map(int, input().split()))
ans = l[0] * (l[0] + 1) * l[1] * (l[1] + 1) * l[2] * (l[2] + 1) // 8 % 998244353
print(ans)
