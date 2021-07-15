q = int(input())
for i in range(q):
    n = int(input())
    prices_sum = sum(list(map(int, input().split())))
    print(prices_sum // n + bool(prices_sum % n))

