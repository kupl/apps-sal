a = int(input())
b = int(input())
n = a + b + 1
print(' '.join(map(str, list(range(n - a, n + 1)) + list(range(1, n - a))[::-1])))
