fib = [1, 1]
fibs = set()
fibs.add(1)
for i in range(50):
    fib.append(fib[-1] + fib[-2])
    fibs.add(fib[-1])
for i in range(1, int(input()) + 1):
    print("O" if i in fibs else "o", end="")
