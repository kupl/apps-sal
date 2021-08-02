n, m = map(int, input().split())

a = n // m
print(['NO', 'YES'][a % 2])
