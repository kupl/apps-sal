def isPrime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True


n = int(input())
if isPrime(n):
    ans = [n]
else:
    bigPrime = 0
    for i in range(n - 1, 0, -1):
        if isPrime(i):
            bigPrime = i
            break

    ans = [bigPrime]
    n -= bigPrime

    if isPrime(n):
        ans.append(n)
    else:
        for i in range(1, n):
            j = n - i
            if isPrime(i) and isPrime(j):
                ans.append(i)
                ans.append(j)
                break

print(len(ans))
for i in ans:
    print(i, end=' ')
