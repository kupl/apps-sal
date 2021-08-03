N = int(input())
r = N % 11
print(N // 11 * 2 + (0 if r == 0 else (1 if r <= 6 else 2)))
