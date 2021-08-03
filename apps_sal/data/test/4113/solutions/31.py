N = int(input())
print("Yes" if any((N - 4 * a >= 0) and (N - 4 * a) % 7 == 0 for a in range(100)) else "No")
