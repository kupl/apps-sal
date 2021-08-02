a, b = map(int, input().split())
result = 0
for i in range(2):
    if a > b:
        result += a
        a -= 1
    else:
        result += b
        b -= 1
print(result)
