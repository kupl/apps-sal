(a, b, c) = list(map(int, input().split()))
result = 'No'
if a + b == c or a + c == b or a == b + c:
    result = 'Yes'
print(result)
