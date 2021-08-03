n = int(input())

fib = [1, 1]

while fib[-1] < n:
    fib.append(fib[-1] + fib[-2])

fib = set(fib)

print(''.join([('o', 'O')[i in fib] for i in range(1, n + 1)]))
