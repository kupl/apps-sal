import math


def trial_division(n):
    factor = []
    tmp = int(math.sqrt(n)) + 1
    for num in range(2, tmp):
        while n % num == 0:
            n //= num
            factor.append(num)
    if not factor:
        factor.append(1)
        factor.append(n)
        return factor
    else:
        factor.append(1)
        factor.append(n)
        return factor


(A, B) = list(map(int, input().split()))
A_primes = trial_division(A)
B_primes = trial_division(B)
primes = []
for p in A_primes:
    if p in B_primes:
        primes.append(B_primes.pop(B_primes.index(p)))
print(len(list(set(primes))))
