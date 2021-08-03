X, Y = list(map(int, input().split()))

print(('Alice' if abs(X - Y) > 1 else 'Brown'))
