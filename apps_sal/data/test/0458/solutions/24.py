(a, b, c) = map(int, input().split())
MAXNUM = 10 ** 9 + 1
ans = ''
ansCount = 0


def s(x):
    result = 0
    while x > 0:
        result += x % 10
        x = x // 10
    return result


for i in range(1, 82):
    num = b * i ** a + c
    if num > 0 and num < MAXNUM and (s(num) == i):
        ans = ans + str(num) + ' '
        ansCount += 1
print(ansCount)
if ansCount > 0:
    print(ans)
