(A, B, C) = list(map(int, input().split()))
a_sum = A * (A + 1) // 2
b_sum = B * (B + 1) // 2
c_sum = C * (C + 1) // 2
ans = a_sum * b_sum * c_sum % 998244353
print(ans)
