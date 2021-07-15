n = int(input())
fib = [1, 1]
for i in range(2, 200):
    fib.append(fib[i - 1] + fib[i - 2])
for i in range(1, n + 1):
    if i in fib:
        print('O', end='')
    else:
        print('o', end='')
