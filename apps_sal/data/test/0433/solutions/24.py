
n, a, b = map(int, input().split())
a -= 1

print(((a + b + n * 1000) % n) + 1)
