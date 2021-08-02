l, r, k = list(map(int, input().split()))

n = 1
numbers = []

while n <= r:
    if n >= l:
        numbers.append(n)

    n *= k

if len(numbers) > 0:
    print(' '.join(map(str, numbers)))
else:
    print('-1')
