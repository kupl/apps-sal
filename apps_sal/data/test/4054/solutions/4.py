
a = list(map(int, input().split()))
b = [1, 1, 2, 7, 4]

print(min([x // y for x, y in zip(a, b)]))
