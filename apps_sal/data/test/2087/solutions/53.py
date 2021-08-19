(A, B, C) = list(map(int, input().split()))
total_c = (1 + C) * C // 2
total_b = (1 + B) * B // 2
total_a = (1 + A) * A // 2
ans = total_a * total_b * total_c % 998244353
print(ans)
