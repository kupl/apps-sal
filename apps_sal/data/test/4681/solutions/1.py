n = int(input())


def fibonacci(n):
    fib = [2, 1]
    for i in range(2, n):
        fib.append(fib[i - 2] + fib[i - 1])
    return fib[n - 1]


print(fibonacci(n + 1))
