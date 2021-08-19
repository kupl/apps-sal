(X, Y) = map(int, input().split())
result = 'No'
for a in range(X + 1):
    b = X - a
    if 2 * a + 4 * b == Y:
        result = 'Yes'
print(result)
