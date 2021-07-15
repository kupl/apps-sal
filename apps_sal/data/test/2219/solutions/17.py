t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    summ = 0
    while n > 0:
        if n % k == 0:
            summ += 1
            n //= k
        else:
            summ += n % k
            n = n - n % k
    print(summ)
