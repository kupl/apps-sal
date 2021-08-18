
A, B = list(map(int, input().split()))

result = A + B
if result >= 24:
    result -= 24

print(result)
