def calc(k):
    cur = 7 % k
    for i in range(1, k + 1):
        if cur == 0:
            return i
        else:
            cur *= 10
            cur += 7
            cur %= k
    return -1


k = int(input())
print(calc(k))
