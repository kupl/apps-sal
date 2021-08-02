t = int(input())
for i in range(t):
    n = int(input())
    k = 4
    while n % (k - 1) != 0:
        k *= 2
    print(n // (k - 1))
