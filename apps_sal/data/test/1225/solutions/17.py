h = int(input())


def wa(n):
    w = 0
    for i in range(0, n + 1):
        w += 2**i
    return w


n = 1
cnt = -1
while n <= h:
    n = n * 2
    cnt += 1
print(wa(cnt))
