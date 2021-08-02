a, b = map(int, input().split())
print('YNeos'[a * b % 2 < 1::2])
