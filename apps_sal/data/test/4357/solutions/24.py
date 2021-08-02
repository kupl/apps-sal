A, B, C = map(int, input().split())
print(max(A * 10 + B + C, B * 10 + A + C, C * 10 + B + A))
