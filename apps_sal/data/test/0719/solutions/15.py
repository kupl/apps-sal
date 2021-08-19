k = int(input())


def DigitSum(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
        if res > 10:
            return 100
    return res


def IsPretty(n):
    return DigitSum(n) == 10


i = 10
while k > 0:
    i += 9
    if IsPretty(i):
        k -= 1
print(i)
