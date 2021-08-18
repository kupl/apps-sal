def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    sqN = int(pow(n, .5))
    while i <= sqN:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True


n = int(input().strip())
arr = [0] * (n + 1)
c = 1
for i in range(2, n + 1):
    if isPrime(i):
        arr[i] = c
        for j in range(i + i, n + 1, i):
            if not arr[j]:
                arr[j] = c
        c += 1
print(*arr[2:])
