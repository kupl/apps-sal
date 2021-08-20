def findSumOfDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return int(sum)


(N, a, b) = map(int, input().split())
c = 0
total = 0
for i in range(N + 1):
    c = findSumOfDigits(i)
    if a <= c <= b:
        total += i
print(total)
