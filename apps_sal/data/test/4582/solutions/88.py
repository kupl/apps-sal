a, b = input().split()

if a == 'H' and b == 'H':
    result = 'H'

if a == 'D' and b == 'H':
    result = 'D'

if a == 'D' and b == 'D':
    result = 'H'

if a == 'H' and b == 'D':
    result = 'D'

print(result)
