a, b = map(int, input().split(" "))
print([a + b, b - a][b % a > 0])
