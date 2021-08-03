A, B = map(int, input().split())
print([-1, c := -min(-A * 100 // 8, -B * 10)][c < min((A + 1) * 100 // 8, B * 10 + 10)])
