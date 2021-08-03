A, B, C = list(map(int, input().split()))

ans = A * (A + 1) // 2 * B * (B + 1) // 2 * C * (C + 1) // 2 % 998244353
ans = int(ans)

print(ans)
