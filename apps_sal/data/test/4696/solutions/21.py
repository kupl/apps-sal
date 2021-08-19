(a, b) = map(int, input().split())
print(['Odd', 'Even'][a * b % 2 == 0])
