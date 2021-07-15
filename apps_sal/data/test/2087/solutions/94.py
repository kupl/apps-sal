A, B, C = map(int, input().split())

d = 998244353

sumA = (A * (A + 1)) // 2
sumB = (B * (B + 1)) // 2
sumC = (C * (C + 1)) // 2

ans = (sumA * sumB * sumC) % d

print(ans)
