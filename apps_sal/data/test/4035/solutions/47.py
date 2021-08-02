A, B = map(int, input().split())
print([-1, c := -min(-A * 25 // 2, -B * 10)][(A + 1) * 25 > c * 2 < B * 20 + 20])
