

a, b, c = list(map(int, input().split()))

result = 0

if a == b:
    result = c
elif b == c:
    result = a
elif a == c:
    result = b
else:
    result = "Error"

print(result)
