q = int(input())
for i in range(q):
    n, k = [int(x) for x in input().split()]
    counter = 0
    while n != 0:
        x = n % k
        n -= x
        counter += x + 1
        n //= k
    print(counter - 1)
