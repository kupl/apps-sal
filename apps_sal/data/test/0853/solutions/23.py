(n, t) = (int(input()), input())
a = t.count('5')
b = n - a
print(int('5' * (a - a % 9) + '0' * b) if b else -1)
