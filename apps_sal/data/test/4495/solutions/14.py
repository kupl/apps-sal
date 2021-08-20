(a, b, x) = list(map(int, input().split()))
print(b // x - a // x + (a % x == 0))
