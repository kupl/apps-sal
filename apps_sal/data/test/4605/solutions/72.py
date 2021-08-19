(n, a, b) = list(map(int, input().split()))
s = 0
ans = 0


def findSumOfDigits(num):
    s = 0
    while num > 0:
        s += int(num % 10)
        num = int(num / 10)
    return s


for i in range(n + 1):
    s = findSumOfDigits(i)
    if a <= s <= b:
        ans += i
print(ans)
