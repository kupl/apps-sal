def findSumOfDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


ans = 0
n = int(input())
total = findSumOfDigits(n)
if n % total == 0:
    print('Yes')
else:
    print('No')
