A, B = map(int, input().split())
print([max(a := 0 - -A * 25 // 2, c := B * 10), -1][c + 10 <= a or (A + 1) * 25 // 2 <= c])
