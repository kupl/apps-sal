import math


def s(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum


a, b, c = map(int, input().split())
ans = []
for i in range(82):
    x = b * i ** a + c
    if x > 0 and x < 10**9 and s(x) == i:
        ans.append(x)
print(len(ans))
if len(ans) > 0:
    for x in ans:
        print(x, end=" ")
