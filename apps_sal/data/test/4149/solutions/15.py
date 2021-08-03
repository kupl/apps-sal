n = int(input())
b = list(map(int, input().split(' ')))

primes = {}
# p=[2]
index = 2
primes[2] = 1

for i in range(4, 2750132, 2):
    primes[i] = -2

for i in range(3, 2750132, 2):
    if primes.get(i) is None:
        # p.append(i)
        multiple = i * i
        primes[i] = index
        index += 1
        while multiple < 2750132:
            if primes.get(multiple) is None:
                primes[multiple] = -i
            multiple += i

# print(len(p))
b.sort(reverse=True)

carr = {}
for c in b:
    if carr.get(c) is None:
        carr[c] = 1
    else:
        carr[c] += 1

# print(b)
k = 0
for c in b:
    if k == n:
        break
    if carr[c] > 0:
        if primes[c] > 0:
            print(primes[c], end=' ')
            carr[c] -= 1
            carr[primes[c]] -= 1
        else:
            print(c, end=' ')
            carr[c] -= 1
            carr[c // (-1 * primes[c])] -= 1
        k += 1
