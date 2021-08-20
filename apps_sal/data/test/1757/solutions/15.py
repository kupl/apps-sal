N = int(input())
fib = [0, 1]
while fib[-1] < 1000:
    fib.append(fib[-1] + fib[-2])
for i in range(1, N + 1):
    print('O' if i in fib else 'o', end='')
print()
