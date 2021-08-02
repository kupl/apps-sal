import math
t = int(input())
for _ in range(t):
    n = int(input())
    divisors = set(n // i for i in range(1, int(math.sqrt(n)) + 1))
    for d in divisors.copy():
        divisors.add(n // d)
    divisors.add(0)

    print(len(divisors))
    print(*sorted(divisors))
