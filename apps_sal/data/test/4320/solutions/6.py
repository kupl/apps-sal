t = int(input())
for i in range(t):
    n = int(input())
    d = 2
    while True:
        if n % (2**d - 1) == 0: print(n // (2**d - 1)); break
        d += 1
