try:

    def isPrime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def printPrime(n):
        l1 = []
        for i in range(2, n + 1):
            if isPrime(i):
                l1.append(i)
        print(len(l1))

    def __starting_point():
        n = int(input())
        printPrime(n)
except:
    pass
__starting_point()
