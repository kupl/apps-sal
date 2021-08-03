n = int(input())
a = 1
b = 1
fib = [0 for i in range(1005)]
fib[1] = 1
for i in range(20):
    try:
        a, b = b, a + b
        fib[b] = 1
    except:
        break
for i in range(1, n + 1):
    if fib[i] == 1:
        print('O', end='')
    else:
        print('o', end='')
print()
