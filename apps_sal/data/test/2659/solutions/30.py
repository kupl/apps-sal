K = int(input())


def minSunuke(n):
    sumDigit = sum(map(int, list(str(n))))
    return n / sumDigit


digit = 0
now = 1
for i in range(K):
    print(now)
    if minSunuke(now + 10 ** digit) > minSunuke(now + 10 ** (digit + 1)):
        digit += 1
    now += 10 ** digit
