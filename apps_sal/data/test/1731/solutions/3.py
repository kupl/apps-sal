import math

MOD = 1000000007

def main():
    (n, m) = ([int(x) for x in input().split()])
    m *= 2
    a = [0] * n
    a[0] = 1
    for i in range(m):
        b = [0] * n
        sum = a[0]
        b[0] = a[0]
        for j in range(1, n):
            sum = (sum + a[j]) % MOD
            b[j] = sum
        a = b
    result = 0
    for i in range(n):
        result = (result + a[i]) % MOD
    print(result)

def __starting_point():
    main()

__starting_point()
