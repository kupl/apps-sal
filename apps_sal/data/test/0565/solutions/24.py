def read():
    return int(input())


def readlist():
    return list(map(int, input().split()))


def readmap():
    return map(int, input().split())


(y, b, r) = readmap()
b -= 1
r -= 2
print(3 * min(y, b, r) + 3)
