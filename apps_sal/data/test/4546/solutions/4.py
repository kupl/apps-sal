(a, b, c) = list(map(int, input().split()))
result = 'NO'
if b - a == c - b:
    result = 'YES'
elif a - b == b - c:
    result = 'YES'
print(result)
