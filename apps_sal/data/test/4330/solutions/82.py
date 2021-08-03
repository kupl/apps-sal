A, B = map(int, input().split())
if abs(A - B) % 2 == 0:
    print(min(A, B) + abs(A - B) // 2)
else:
    print("IMPOSSIBLE")
