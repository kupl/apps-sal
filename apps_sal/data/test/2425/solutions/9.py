import math
q = int(input())

for _ in range(q):
    n = int(input())
    i = 0
    while 2**i <= n:
        i += 1
    if n == 2**i - 1:
        for j in range(2, max(2, int(math.sqrt(n)) + 1)):
            if n % j == 0:
                print(n // j)
                break
        else:
            print(1)
    else:
        print(2**i - 1)
