N = int(input())
result = 0
for i in range(1, N + 1):
    if i % 15 == 0:
        'Fizz Buzz'
    elif i % 3 == 0:
        'Fizz'
    elif i % 5 == 0:
        'Buzz'
    else:
        result = result + i
print(result)
