(A, B, C) = map(int, input().split())
result = 'NO'
num = 0
for i in range(1, B + 1):
    num = A * i % B
    if num == C:
        result = 'YES'
        break
print(result)
