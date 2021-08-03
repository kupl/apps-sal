A, B = int(input()), int(input())

print(*range(B + 1, A + B + 2), *reversed(range(1, B + 1)))
