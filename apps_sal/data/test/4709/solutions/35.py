a, op, b = map(str, input().split())
a = int(a)
b = int(b)

if op == "+":
    result = a + b
else:
    result = a - b

print(result)
