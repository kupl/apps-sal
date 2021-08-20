(A, B) = map(int, input().split())
result = A + B
if result <= A - B:
    result = A - B
if result <= A * B:
    result = A * B
print(result)
