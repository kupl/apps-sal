import math
primes = [2]
n = int(input())
curr_num = 1
res = [1]
for i in range(3, n + 1):
    is_prime = True
    limit = math.ceil(math.sqrt(i))
    for p in primes:
        if i % p == 0:
            res.append(res[p - 2])
            is_prime = False
            break
        if p > limit:
            break
    if is_prime:
        curr_num += 1
        res.append(curr_num)
        primes.append(i)
print(' '.join(map(str, res)))
