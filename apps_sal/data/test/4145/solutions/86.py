sieve = [False for i in range(200000)]
for i in range(2, len(sieve)):
    if not sieve[i]:
        for j in range(i * i, len(sieve), i):
            sieve[j] = True
x = int(input())
for i in range(2, len(sieve)):
    if (not sieve[i]) and i >= x:
        print(i)
        return
