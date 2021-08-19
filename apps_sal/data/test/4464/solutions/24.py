(a, b, c) = map(int, input().split())
result = 'NO'
for i in range(1, b):
    if a * i % b == c:
        result = 'YES'
        break
print(result)
