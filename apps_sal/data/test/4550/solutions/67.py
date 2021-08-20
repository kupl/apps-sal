(a, b, c) = map(int, input().split())
print(['No', 'Yes'][a + b == c or a + c == b or b + c == a])
