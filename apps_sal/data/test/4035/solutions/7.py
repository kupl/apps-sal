(A, B) = map(int, input().split())
print([-1, (c := (-min(-A * 50 // 4, -B * 10)))][c < min((A + 1) * 50 // 4, B * 10 + 10)])
