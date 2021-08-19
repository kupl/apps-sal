(A, B) = map(int, input().split())
c = max(-(-A * 100 // 8), B * 10)
d = min((A + 1) * 100 // 8, B * 10 + 10)
print([-1, c][c < d])
