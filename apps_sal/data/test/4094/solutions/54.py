K = int(input())


def calc(K):
    if K % 2 == 0:
        return -1
    seven = 0
    for i in range(1, K + 1):
        seven *= 10
        seven += 7
        seven %= K
        if seven == 0:
            return i
    return -1


print(calc(K))
