(A, B) = map(int, input().split())
print([max((a := (0 - -A * 25 // 2)), (c := (B * 10))), -1][~(a - 10 < c < (A + 1) * 25 // 2)])
