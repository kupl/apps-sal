(a, b, c) = map(int, input().split())
sumA = a * (a + 1) // 2
sumB = b * (b + 1) // 2
sumC = c * (c + 1) // 2
print(sumA * sumB * sumC % 998244353)
