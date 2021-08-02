a = int(input())
fib = [1, 2]
for i in range(100):
    fib.append(fib[-1] + fib[-2])

for i in range(1, 1000):
    if fib[i] <= a < fib[i + 1]:
        print(i)
        quit()
