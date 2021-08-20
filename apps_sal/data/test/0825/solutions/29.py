n = int(input())
m = n
primes = {}
for i in range(2, int(n ** 0.5 + 2)):
    while m % i == 0:
        m //= i
        if i not in primes:
            primes[i] = 1
        else:
            primes[i] += 1
    if i > m:
        break
if m != 1:
    primes[m] = 1
cnt = 0
num = 0
flag = True
while flag == True:
    num += 1
    flag = False
    for i in primes:
        if 0 < primes[i] <= num * 2:
            cnt += 1
            primes[i] = 0
        elif primes[i] > num * 2:
            cnt += 1
            flag = True
            primes[i] -= num
print(cnt)
