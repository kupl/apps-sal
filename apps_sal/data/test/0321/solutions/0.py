def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True


t = int(input())
for yes in range(t):
    a, b = map(int, input().split())
    xx = a - b
    yy = a + b
    if xx == 1 and isPrime(yy) == True:
        print("YES")
    else:
        print("NO")
