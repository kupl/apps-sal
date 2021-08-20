a = int(input())
b = int(input())
n = abs(a - b) // 2
print(n * (n + 1) + abs(a - b) % 2 * (n + 1))
