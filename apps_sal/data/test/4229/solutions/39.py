n = int(input())
out = n * (n + 1) // 2
u = n // 5
out -= u * (u + 1) // 2 * 5
u = n // 3
out -= u * (u + 1) // 2 * 3
u = n // 15
out += u * (u + 1) // 2 * 15
print(out)
