import math
n = int(input())


def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor


dlist = list(divisorGenerator(n))
dlist.sort(key=lambda x: -x)
fun = []
for d in dlist:
    number = n // d
    fun.append(number * (number + 1) // 2 * d - number * (d - 1))
print(*fun)
