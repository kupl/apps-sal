try:
    def isPrime(n):

        if n <= 1:
            return False

        for i in range(2, n):
            if n % i == 0:
                return False

        return True

    def printPrime(n):
        count = 0
        for i in range(2, n + 1):
            if isPrime(i):
                count = count + 1
        print(count)

    n = int(input())
    printPrime(n)
except:
    pass
