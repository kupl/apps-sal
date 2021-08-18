
A, B = list(map(int, input().split()))

result = 'Impossible'

if A % 3 == 0 or B % 3 == 0 or (A + B) % 3 == 0:
    result = 'Possible'

print(result)
