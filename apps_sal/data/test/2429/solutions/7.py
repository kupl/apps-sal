for _ in range(int(input())):
    n = int(input())
    a = 2**n
    b = 0
    for i in range(n//2):
        b += 2**(n-i-1)
    for i in range(1, n//2):
        a += 2**i
    print(abs(a-b))

