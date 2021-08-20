import itertools
n = int(input())
numbers = list(map(int, input().split()))


def canMakeTriangle(a, b, c):
    return a < b + c and b < a + c and (c < a + b)


def isDifferentLength(a, b, c):
    return a != b and b != c and (c != a)


def isTargetTriangle(a, b, c):
    return isDifferentLength(a, b, c) and canMakeTriangle(a, b, c)


total = 0
for (a, b, c) in list(itertools.combinations(numbers, 3)):
    if isTargetTriangle(a, b, c):
        total += 1
print(total)
