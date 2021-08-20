(A, B) = map(int, input().split())
print('IMPOSSIBLE' if (A + B) % 2 > 0 else (A + B) // 2)
