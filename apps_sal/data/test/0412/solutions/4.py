from math import log2


def c(a, b):
    for i in a:
        if i % b == 0:
            return True
    return False


def cnt(a, b):
    ans = 0
    for i in a:
        if i % b == 0:
            ans += 1
    return ans


input()
a = [int(i) for i in input().split()]
b = 2
while c(a, b):
    b *= 2
print(b // 2, cnt(a, b // 2))
