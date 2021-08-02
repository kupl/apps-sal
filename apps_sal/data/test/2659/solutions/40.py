K = int(input())


def sunuke(n):
    sumN = sum(map(int, list(str(n))))
    return n / sumN


digit = 0
now = 1

for i in range(K):
    print(now)
    if sunuke(now + 10**digit) > sunuke(now + 10**(digit + 1)):
        digit += 1
    now += 10**digit
