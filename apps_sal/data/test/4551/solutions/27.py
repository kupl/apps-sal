
A, B, C, D = list(map(int, input().split()))

ab = A + B
cd = C + D
result = 'Balanced'

if ab > cd:
    result = 'Left'
elif ab < cd:
    result = 'Right'

print(result)
