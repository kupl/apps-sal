try:
    def isPrime(n):

        # Corner case
        if n <= 1:
            return False

    # check from 2 to n-1
        for i in range(2, n):
            if n % i == 0:
                return False

        return True

# Function to print primes
    def printPrime(n):
        l1 = []
        for i in range(2, n + 1):
            if isPrime(i):
                l1.append(i)

        print(len(l1))

# Driver code
    def __starting_point():
        n = int(input())
    # function calling
        printPrime(n)
except:
    pass
__starting_point()
