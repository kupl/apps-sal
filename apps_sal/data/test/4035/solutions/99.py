A, B = map(int, input().split())
print([-1, max(a := 0 - -A * 25 // 2, c := B * 10)][a - 10 < c < (A + 1) * 25 // 2])
