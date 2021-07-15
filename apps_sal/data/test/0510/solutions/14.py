a, b, c, d = map(int, input().split())
A = [a, b, c]
a, b, c = sorted(A)
print(max(0, d - abs(a-b)) + max(0, d - abs(c-b)))
